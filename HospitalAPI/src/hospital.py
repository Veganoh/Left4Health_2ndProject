
class Hospital:
    id = None
    name = None
    address = None

    current_wait_time_pacient = None
    distance_from_current_pacient = None
    duration_from_current_pacient = None

    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address


    #hospital to string
    def __str__(self):
        return f"{self.id} - {self.current_wait_time_pacient} - {self.duration_from_current_pacient} - {self.distance_from_current_pacient}"
