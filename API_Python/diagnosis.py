import json
import joblib
import pandas as pd
import os

def choose_model(model_num_str):
    model_num= int(model_num_str)
  
    if model_num==1:
        model_name="svm"
    elif model_num==2:
        model_name="adaboost"
    else:
        model_name="xgboost"

    #Load model from Models folder
    modelPath = os.path.abspath("../Models/"+model_name+'/'"model_"+model_name+'.joblib')
    model = joblib.load(modelPath)
    return model

def get_diagnosis(patient_data):


    model=choose_model(patient_data['model'])

    #Female	Age	Injured	Pain	NRS_pain	HR	RR	BT	Saturation	KTAS_expert	Mental_Alert	Mental_Pain Response	Mental_Unresponsive	Mental_Verbal Response	Arrival mode_Other	Arrival mode_Private Ambulance	Arrival mode_Private Vehicle	Arrival mode_Public Ambulance	Arrival mode_Public Transport	Arrival mode_Walking	Arrival mode_Wheelchair	Blood Pressure_Elevated	Blood Pressure_Hypertension	Blood Pressure_Hypertensive crises	Abdominal Pain	Dyspnea	Dizziness	Fever	Anterior Chest Pain	Open Wound	Headache	Epigastric Pain	Mental Change	General Weakness	Vomiting	Chest Pain
    columns = ['Female','Age','Injured','Pain','NRS_pain',
            'HR','RR','BT','Saturation',
            'Mental_Alert','Mental_Pain Response','Mental_Unresponsive','Mental_Verbal Response',
            'Arrival mode_Other','Arrival mode_Private Ambulance','Arrival mode_Private Vehicle',
            'Arrival mode_Public Ambulance','Arrival mode_Public Transport','Arrival mode_Walking',
            'Arrival mode_Wheelchair','Blood Pressure_Elevated','Blood Pressure_Hypertension',
            'Blood Pressure_Hypertensive crises','Abdominal Pain','Dyspnea','Dizziness','Fever',
            'Anterior Chest Pain','Open Wound','Headache','Epigastric Pain','Mental Change',
            'General Weakness','Vomiting','Chest Pain']
    

    #Create a dataframe with the patient data in respective columns 
    data = pd.DataFrame(columns = columns) 
    data.columns = data.columns.astype(str)

    processed_patiente_data={
        'Female': int(patient_data['sex']),  
        'Age': int(patient_data["age"]),  
        'Injured':  int(patient_data["injured"]), 
        'Pain':int(patient_data["pain"]),
        'NRS_pain': int(patient_data["nrs_pain"]),  
        'HR': float(patient_data["heart_rate"]), 
        'RR': float(patient_data["respiratory_rate"]), 
        'BT': float(patient_data["temperature"]), 
        'Saturation': float(patient_data["saturation"]), 
    }

    #Append the processed patient data as a new row to the DataFrame
    data.loc[len(data)] = processed_patiente_data

    #Processed data from mental_state
    mental_state_map={
        'alert':'Mental_Alert',
        'painResponse': 'Mental_Pain Response',
        'unresponsive': 'Mental_Unresponsive',
        'verbalResponse': 'Mental_Verbal Response',
    }

    select_mental_state= mental_state_map.get(patient_data["mental_state"], None)

    if select_mental_state:
        data.loc[len(data) - 1,select_mental_state] = 1

    #Processed data from arrival_mode
    arrival_mode_map={
        'other': 'Arrival mode_Other',
        'privateAmbulance': 'Arrival mode_Private Ambulance',
        'privateVehicle': 'Arrival mode_Private Vehicle',
        'publicAmbulance': 'Arrival mode_Public Ambulance',
        'publicTransport': 'Arrival mode_Public Transport',
        'walking': 'Arrival mode_Walking',
        'wheelchair': 'Arrival mode_Wheelchair',
    }

    select_arrival_mode=arrival_mode_map.get(patient_data["arrival_mode"], None)

    if select_arrival_mode:
        data.loc[len(data) - 1,select_arrival_mode]=1

    #Processed data from blood_pressure
    blood_pressure_map={
        'elevated': 'Blood Pressure_Elevated',
        'hypertension': 'Blood Pressure_Hypertension',
        'hypertensiveCrises': 'Blood Pressure_Hypertensive crises',
    }

    select_blood_pressure=blood_pressure_map.get(patient_data["blood_pressure"], None)

    if select_blood_pressure:
        data.loc[len(data) - 1,select_blood_pressure]=1

    #Processed data from blood_pressure
    symptom_map= {
        'abdominalPain': 'Abdominal Pain',
        'dyspnea': 'Dyspnea',
        'dizziness': 'Dizziness',
        'fever': 'Fever',
        'chestPain': 'Anterior Chest Pain',
        'openWound': 'Open Wound',
        'headache': 'Headache',
        'epigastricPain': 'Epigastric Pain',
        'mentalChange': 'Mental Change',
        'generalWeakness': 'General Weakness',
        'vomiting': 'Vomiting',
    }

    select_symptom=symptom_map.get(patient_data["symptom"], None)

    if select_symptom:
        data.loc[len(data) - 1,select_symptom]=1


    #Fill null with 0
    data = data.fillna(0)

    print(f"DATAAAA: {data}")

    # Check if there is at least one sample in the data
    if data.shape[0] == 0:
        print("Dados de teste vazios. Não é possível fazer previsões.")
        return None
    
    #Predict the diagnosis
    prediction = model.predict(data)
    patient_prediction= prediction[0]
    print(f"Predict: {patient_prediction}")
    
    return patient_prediction
    

