class Hospital:
    id = None
    name = None
    address = None

    def __init__(self, id, name, address, wait_time):
        self.id = id
        self.name = name
        self.address = address
        self.wait_time = wait_time


    #hospital to string
    def __str__(self):
        return f"{self.id} - {self.name}"
