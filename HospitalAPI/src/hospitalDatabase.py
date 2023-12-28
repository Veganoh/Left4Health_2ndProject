import requests
import json
from hospital import Hospital
from concurrent.futures import ThreadPoolExecutor

class HospitalDatabase:
    MAX_RETRIES = 2
    INSTITUTION_URL = "https://tempos.min-saude.pt/api.php/institution"
    STANDBY_TIME_URL = "https://tempos.min-saude.pt/api.php/standbyTime/"
    GENERAL_URGENCY_DESCRIPTIONS = {"Urgência Geral", "Urgencia Geral", "Urg. Geral", "SERVICO URGENCIA BASICO"}

    def __init__(self):
        self.hospitals = []

    def __str__(self):
        return "\n".join(str(hospital) for hospital in self.hospitals)

    def get_hospital_by_id(self, id):
        return next((hospital for hospital in self.hospitals if hospital.id == id), None)

    def fetch_and_process_hospitals_data(self):
        try:
            response = requests.get(self.INSTITUTION_URL)
            response.raise_for_status()
            data = json.loads(response.content.decode("utf-8-sig"))

            hospitals_data = data.get("Result", [])
            self.hospitals = [Hospital(id=hospital["Id"], name=hospital["Name"], address=hospital["Address"])
                              for hospital in hospitals_data if hospital.get("HasEmergency", False)]

            self.get_waiting_times()

        except requests.RequestException as e:
            print(f"Failed to fetch or process data. Error: {e}")

    def get_waiting_times(self):
        try:
            with ThreadPoolExecutor() as executor:
                futures = [executor.submit(self.fetch_hospital_waiting_times, hospital) for hospital in self.hospitals]
                wait_times = [future.result() for future in futures]

                for hospital, wait_time in zip(self.hospitals, wait_times):
                    hospital.wait_time = wait_time

        except requests.RequestException as e:
            print(f"Failed to fetch or process data. Error: {e}")

    def fetch_hospital_waiting_times(self, hospital):
        for retry in range(self.MAX_RETRIES + 1):
            try:
                response = requests.get(f"{self.STANDBY_TIME_URL}{hospital.id}", timeout=10)
                response.raise_for_status()

                content = response.content.decode("utf-8-sig")

                if content:
                    data = json.loads(content)
                    urgency_general_queues = [
                        queue for queue in data.get("Result", [])
                        if queue.get("Emergency", {}).get("Description") in self.GENERAL_URGENCY_DESCRIPTIONS
                    ]

                    if urgency_general_queues:
                        first_occurrence = urgency_general_queues[0]
                        return {
                            "Red": first_occurrence.get("Red", {}),
                            "Orange": first_occurrence.get("Orange", {}),
                            "Yellow": first_occurrence.get("Yellow", {}),
                            "Green": first_occurrence.get("Green", {}),
                            "Blue": first_occurrence.get("Blue", {}),
                        }
                    else:
                        return {}
                else:
                    return {}

            except requests.Timeout:
                if retry < self.MAX_RETRIES:
                    pass
                else:
                    return []

            except requests.RequestException:
                return []