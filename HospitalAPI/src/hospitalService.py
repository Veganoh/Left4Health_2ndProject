from routeFetcher import calculate_distance_duration
from topsis import Topsis


class HospitalService:
    duration_times = []
    wait_times = []

    def __init__(self, hospital_db):
        self.hospital_db = hospital_db

    def get_best_alternatives(self, origin, color, weights, transport):
        self.duration_times = calculate_distance_duration(origin, transport, self.hospital_db.hospitals)
        self.wait_times = self.hospital_db.get_hospitals_by_color(color)

        tp = Topsis(self.wait_times, self.duration_times, weights)
        ID1, ID2, ID3 = tp.get_best_alternatives()

        H1 = self.hospital_db.get_hospital_by_id(ID1)
        H2 = self.hospital_db.get_hospital_by_id(ID2)
        H3 = self.hospital_db.get_hospital_by_id(ID3)

        return {
            "hospital1": self.get_hospital_dict(H1),
            "hospital2": self.get_hospital_dict(H2),
            "hospital3": self.get_hospital_dict(H3),
        }

    def get_hospital_string(self, hospital):
        return f"{hospital.id} - {hospital.name} - {hospital.address}"

    def get_hospital_dict(self, hospital):
        return {
            "id": hospital.id,
            "name": hospital.name,
            "address": hospital.address,
            "wait_time": self.get_waiting_time_by_id(self.wait_times, hospital.id),
            "duration": self.get_duration_by_id(self.duration_times, hospital.id),
            "latitude": hospital.latitude,
            "longitude": hospital.longitude,

        }

    def get_waiting_time_by_id(self, waiting_time_list, id):
        waiting_time = None

        for item_waiting_time in waiting_time_list:
            if item_waiting_time['ID'] == id:
                waiting_time = item_waiting_time['Wait Time']
                break

        return waiting_time

    def get_duration_by_id(self, duration_list, id):
        duration = None

        for item_duration in duration_list:
            if item_duration['ID'] == id:
                duration = item_duration['Duration']
                break

        return duration
