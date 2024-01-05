class Hospital:
    id = None
    name = None
    address = None
    current_wait_time = None

    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address


    #hospital to string
    def __str__(self):
        return f"{self.id} - {self.name} - {self.address} "

    def get_wait_time(self, color):
        if isinstance(self.current_wait_time, dict):
            return self.current_wait_time.get(color)
        else:
            return 999999999  # or handle the case where self.current_wait_time is not a dictionary

