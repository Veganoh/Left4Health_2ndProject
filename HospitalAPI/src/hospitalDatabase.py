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
            self.process_waiting_times()

        except requests.RequestException as e:
            print(f"Failed to fetch or process data. Error: {e}")

    def process_waiting_times(self):
        try:
            with ThreadPoolExecutor() as executor:
                futures = [executor.submit(self.fetch_hospital_waiting_times, hospital) for hospital in
                           self.hospitals]
                wait_times = [future.result() for future in futures]

                for hospital, wait_time in zip(self.hospitals, wait_times):
                    hospital.current_wait_time = wait_time

        except requests.RequestException as e:
            print(f"Failed to fetch or process data. Error: {e}")

    def fetch_hospital_waiting_times(self, hospital):
        for retry in range(self.MAX_RETRIES + 1):
            try:
                response = requests.get(f"{self.STANDBY_TIME_URL}{hospital.id}", timeout=1)
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
                            "Red": first_occurrence.get("Red", {}).get("Time",None),
                            "Orange": first_occurrence.get("Orange", {}).get("Time",None),
                            "Yellow": first_occurrence.get("Yellow", {}).get("Time",None),
                            "Green": first_occurrence.get("Green", {}).get("Time",None),
                            "Blue": first_occurrence.get("Blue", {}).get("Time",None),
                        }
                    else:
                        return "N/A"
                else:
                    return "N/A"

            except requests.Timeout:
                if retry < self.MAX_RETRIES:
                    pass
                else:
                    return "N/A"

            except requests.RequestException:
                return "N/A"

        # for a given color gives the pair ID and wait time of each hospital

    def get_hospitals_by_color(self, color):
        hospitals_info = [{"ID": hospital.id, "Wait Time": hospital.get_wait_time(color)} for hospital in self.hospitals]
        hospitals_info.sort(key=lambda x: x['ID'])

        return hospitals_info
