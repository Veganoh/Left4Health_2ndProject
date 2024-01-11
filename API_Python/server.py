from flask import Flask, jsonify, request
from diagnosis import get_diagnosis

app = Flask(__name__)

@app.route('/api/diagnosis', methods=['POST', 'OPTIONS'])
def diagnosis():
    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type',
        }
        return ('', 204, headers)

    patient_data = request.get_json()
    if not patient_data:
        return jsonify({'error': 'Missing required parameters.'}), 400
    else :
        diagnose=get_diagnosis(patient_data)
        diagnose_serializable = int(diagnose)
        response = jsonify({'triage': diagnose_serializable})
        response.headers.add('Access-Control-Allow-Origin', '*')
        print (response)
        return response

@app.route('/api/hello', methods=['GET'])
def hello():
    return "Hello, World!"   


if __name__ == '__main__':
    app.run(debug=True, port=5010)
    