from flask import Flask, render_template, jsonify
from hospitalDatabase import HospitalDatabase
from main import prioritize_hospitals
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Ativar o CORS para permitir solicitações de origens diferentes

@app.route('/')
def index():
    return render_template('suggestions.component.html') 

@app.route('/get_hospitals')
def get_hospitals():
    db = HospitalDatabase()
    db.fetch_hospitals_data()

    # Aqui, você pode adicionar a lógica para obter dados relevantes para o frontend, se necessário

    sorted_hospitals = prioritize_hospitals(db.hospitals)
    hospitals_info = [{"name": hospital.name, "distance": hospital.distance, "wait_time": hospital.wait_time} for hospital in sorted_hospitals]

    return jsonify(hospitals_info)

if __name__ == "__main__":
    app.run(debug=True)