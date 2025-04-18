
from flask import Flask , request , jsonify
import os
app = Flask(__name__)

@app.route('/ModelResponse', methods=['POST'])

def SendModelResponse():
    data = request.json

    if not data or 'SecutitySocre' not in data or 'AvailabilityScore' not in data or 'ProcessingIntegrityScore' not in data or 'ConfidentialityScore' not in data or 'PrivacyScore' not in data or 'TotalScore' not in data or 'Description' not in data:
        return jsonify({"error": "Missing Soc2 Report Analysis in request body"}), 400
    
    # Read Data from response

    securityScore = data['SecutitySocre']
    availabilityScore = data['AvailabilityScore']
    processingIntegrityScore = data['ProcessingIntegrityScore']
    confidentialityScore = data['ConfidentialityScore']
    privacyScore = data['PrivacyScore']
    totalScore = data['TotalScore']
    description = data['Description']

    return jsonify(
                        {
                            "SecutitySocre" : securityScore,
                            "AvailabilityScore" : availabilityScore,
                            "ProcessingIntegrityScore" : processingIntegrityScore, 
                            "ConfidentialityScore" : confidentialityScore,
                            "PrivacyScore" : privacyScore,
                            "TotalScore" : totalScore,
                            "Description" : description
                        }
    )

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use Render's PORT or default to 5000 locally
    app.run(host='0.0.0.0', port=port, debug=False)
