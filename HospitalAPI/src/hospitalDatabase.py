import requests
import json
from hospital import Hospital

class HospitalDatabase:

    # Constructor
    def __init__(self):
        self.hospitals = []

    # HospitalDatabase to string
    def __str__(self):
        return "\n".join(str(hospital) for hospital in self.hospitals)

    # Get Hospital by ID
    def get_hospital_by_id(self, id):
        for hospital in self.hospitals:
            if hospital.id == id:
                return hospital
        return None

    # Fetch Hospitals Data
    def fetch_hospitals_data(self):
        url = "https://tempos.min-saude.pt/api.php/institution"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an HTTPError for bad responses

            data = json.loads(response.content.decode("utf-8-sig"))
            self.process_hospitals_data(data)
        except requests.RequestException as e:
            print(f"Failed to fetch data. Error: {e}")

    # Process Hospitals Data
    def process_hospitals_data(self, data):
        hospitals_data = data.get("Result", [])

        for hospital_data in hospitals_data:
            has_urgency = hospital_data.get("HasEmergency", False)

            if has_urgency:
                hospital = Hospital(
                    id=hospital_data.get("Id"),
                    name=hospital_data.get("Name"),
                    address=hospital_data.get("Address"),
                    wait_time=hospital_data.get("wait_time"),
                )
                self.hospitals.append(hospital)
