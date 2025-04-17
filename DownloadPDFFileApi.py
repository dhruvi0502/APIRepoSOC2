from flask import jsonify , Flask
from flask import request, abort, send_file
from tkinter import Tk, filedialog
import os
import requests
from io import BytesIO
app = Flask(__name__)

@app.route('/download', methods = ['GET'])
def DownloadFile():

    filePath = request.json['filePath'] 
    print(filePath)
     # Optional: Validate and sanitize file path here
    if not filePath:
        return abort(404, description="FilePath Is Missing.")
    
    try:
        response = requests.get(filePath, stream=True)
        if response.status_code != 200:
            return abort(404, description="File could not be downloaded from the URL.")
        
        # Infer filename from URL or default
        filename = filePath.split("/")[-1].split("?")[0]
        if not filename.lower().endswith('.pdf'):
            filename += ".pdf"
        # Create an in-memory buffer
        file_stream = BytesIO(response.content)
        file_stream.seek(0)
        print(f"Sending file: {filename} with size: {len(response.content)} bytes")
        print(f"Headers: {dict(response.headers)}")
        return send_file(
            file_stream,
            as_attachment=True,
            download_name=filename,
            mimetype='application/pdf'
        )
    except Exception as e:
        return abort(500, description=f"Error downloading file: {str(e)}")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use Render's PORT or default to 5000 locally
    app.run(host='0.0.0.0', port=port, debug=False)
