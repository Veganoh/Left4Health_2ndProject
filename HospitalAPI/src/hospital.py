class Hospital:
    id = None
    name = None
    address = None
    wait_time = None

    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address


    #hospital to string
    def __str__(self):
        return f"{self.id} - {self.wait_time}"
