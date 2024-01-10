from flask import Flask, jsonify, request
from diagnosis import PatientData

app = Flask(__name__)

class MyApp:
    def __init__(self):
        self.PatientData = PatientData()

    def get_PatientData(self):
        return self.hospital_service

my_app = MyApp()

@app.route('/api/diagnosis', methods=['GET'])
def diagnosis():
    patient_data = request.get_json()

    if not patient_data:
        return jsonify({'error': 'Missing required parameters.'}), 400
    else :
        diagnose = my_app.PatientData.get_diagnosis(patient_data)
        response = jsonify({'diagnosis' : diagnose})
        print (response)
        return response

   




    