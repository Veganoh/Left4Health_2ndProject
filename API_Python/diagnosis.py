from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import tensorflow as tf
import os

class PatientData:
    def __init__ (self, age , arrival_mode, blood_pressure, heart_rate, injured, mental_state, model, nrs_pain, pain, respiratory_rate, saturation, sex, symptom, temperature):
        self.age = age
        self.arrival_mode = arrival_mode
        self.blood_pressure = blood_pressure
        self.heart_rate = heart_rate
        self.injured = injured
        self.mental_state = mental_state
        self.model = model
        self.nrs_pain = nrs_pain
        self.pain = pain
        self.respiratory_rate = respiratory_rate
        self.saturation = saturation
        self.sex = sex
        self.symptom = symptom
        self.temperature = temperature


    def get_diagnosis(patient_data):

        #Load model from Models folder
        modelPath = os.path.abspath("./Models/"+patient_data.model+'/'+patient_data.model+'.h5')
        model = tf.keras.models.load_model(modelPath)

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

        data['Female'] = patient_data.Sex.values.astype(int)
        data['Age'] = patient_data.Age.values.astype(int)
        data['Injured'] = patient_data.Injured.values.astype(int)
        data['Pain'] = patient_data.Pain.values.astype(int)
        data['NRS_pain'] = patient_data.NRS_pain.values.astype(int)
        data['HR'] = patient_data.HR.values.astype(float)
        data['RR'] = patient_data.RR.values.astype(float)
        data['BT'] = patient_data.BT.values.astype(float)
        data['Saturation'] = patient_data.Saturation.values.astype(float)

        if patient_data.Mental_State == 'alert':
            data['Mental_Alert'] = 1
        elif patient_data.Mental_State == 'painResponse':
            data['Mental_Pain Response'] = 1
        elif patient_data.Mental_State == 'unresponsive':
            data['Mental_Unresponsive'] = 1
        elif patient_data.Mental_State == 'verbalResponse':
            data['Mental_Verbal Response'] = 1
        
        if patient_data.Arrival_Mode == 'other':
            data['Arrival mode_Other'] = 1
        elif patient_data.Arrival_Mode == 'privateAmbulance':
            data['Arrival mode_Private Ambulance'] = 1
        elif patient_data.Arrival_Mode == 'privateVehicle':
            data['Arrival mode_Private Vehicle'] = 1
        elif patient_data.Arrival_Mode == 'publicAmbulance':
            data['Arrival mode_Public Ambulance'] = 1
        elif patient_data.Arrival_Mode == 'publicTransport':
            data['Arrival mode_Public Transport'] = 1
        elif patient_data.Arrival_Mode == 'walking':
            data['Arrival mode_Walking'] = 1
        elif patient_data.Arrival_Mode == 'wheelchair':
            data['Arrival mode_Wheelchair'] = 1

        if patient_data.Blood_Pressure == 'elevated':
            data['Blood Pressure_Elevated'] = 1
        elif patient_data.Blood_Pressure == 'hypertension':
            data['Blood Pressure_Hypertension'] = 1
        elif patient_data.Blood_Pressure == 'hypertensiveCrises':
            data['Blood Pressure_Hypertensive crises'] = 1
        
        if patient_data.Symptom == 'abdominalPain':
            data['Abdominal Pain'] = 1
        elif patient_data.Symptom == 'dyspnea':
            data['Dyspnea'] = 1
        elif patient_data.Symptom == 'dizziness':
            data['Dizziness'] = 1
        elif patient_data.Symptom == 'fever':
            data['Fever'] = 1
        elif patient_data.Symptom == 'chestPain':
            data['Anterior Chest Pain'] = 1
        elif patient_data.Symptom == 'openWound':
            data['Open Wound'] = 1
        elif patient_data.Symptom == 'headache':
            data['Headache'] = 1
        elif patient_data.Symptom == 'epigastricPain':
            data['Epigastric Pain'] = 1
        elif patient_data.Symptom == 'mentalChange':
            data['Mental Change'] = 1
        elif patient_data.Symptom == 'generalWeakness':
            data['General Weakness'] = 1
        elif patient_data.Symptom == 'vomiting':
            data['Vomiting'] = 1

        #fill null with 0
        data = data.fillna(0)

        #Predict the diagnosis
        prediction = model.predict(data)
    
        return prediction