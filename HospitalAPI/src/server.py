from flask import Flask, jsonify, request
from hospitalDatabase import HospitalDatabase
from hospitalService import HospitalService
import diagnosisService

app = Flask(__name__)


class MyApp:
    def __init__(self):
        self.hospital_db = HospitalDatabase()
        self.hospital_db.fetch_and_process_hospitals_data()
        self.hospital_service = HospitalService(self.hospital_db)

    def get_hospital_service(self):
        return self.hospital_service


my_app = MyApp()


@app.route('/api/best_alternatives', methods=['POST', 'OPTIONS'])
def best_alternatives():
    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST',
            'Access-Control-Allow-Headers': 'Content-Type',
        }
        return ('', 204, headers)

    data = request.get_json()

    origin = data.get('origin', '')
    color = data.get('color', '')
    weights = data.get('weights', '')
    transport = data.get('transport', '')

    if not (origin and color and weights and transport):
        return jsonify({'error': 'Missing required parameters.'}), 400

    try:
        weights = [float(w) for w in weights.split(',')]
    except ValueError:
        return jsonify({'error': 'Invalid weights format.'}), 400

    hospital_service = my_app.get_hospital_service()
    best_alternatives = hospital_service.get_best_alternatives(origin, color, weights, transport)

    response = jsonify({'best_alternatives': best_alternatives})
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


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
    else:
        diagnose = diagnosisService.get_diagnosis(patient_data)
        diagnose_serializable = int(diagnose)
        # Adds 1 to the returned value because the prediction ranges from 0-4 and the triage from 1-5
        diagnose_serializable += 1
        response = jsonify({'triage': diagnose_serializable})
        response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    app.run(debug=False)
