from flask import Flask, jsonify, request
from hospitalDatabase import HospitalDatabase
from hospitalService import HospitalService

app = Flask(__name__)

class MyApp:
    def __init__(self):
        self.hospital_db = HospitalDatabase()
        self.hospital_db.fetch_and_process_hospitals_data()
        self.hospital_service = HospitalService(self.hospital_db)

    def get_hospital_service(self):
        return self.hospital_service

my_app = MyApp()

# Rota para obter as melhores alternativas
@app.route('/api/best_alternatives', methods=['POST'])
def best_alternatives():
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
    return jsonify({'best_alternatives': best_alternatives})

if __name__ == '__main__':
    app.run(debug=False)
