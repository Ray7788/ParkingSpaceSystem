class Vehicle:
    def __init__(self, size) -> None:
        self.vehicle_size = size
        # self.layer = 

    def get_size(self):
        return self.vehicle_size
   
class Sedan(Vehicle):
    def __init__(self):
        super().__init__(1)

class Limo(Vehicle):
    def __init__(self):
        super().__init__(2)

class MiniVan(Vehicle):
    def __init__(self):
        super().__init__(2)

class Truck(Vehicle):
    def __init__(self):
        super().__init__(3)

class Driver:
    def __init__(self, id, vehicle):
        self._id = id
        self._vehicle = vehicle
        self._payment_due = 0

    def get_vehicle(self):
        return self._vehicle

    def get_id(self):
        return self._id

    def charge(self, amount):
        self._payment_due += amount