# 1
class Vehicle:
    '''
    base class for vehiles
    '''
    def __init__(self, size):
        ''' 
        decides how much space should this vehicle occupy 
        '''
        self.vehicle_size = size
        # self.layer = 

    def get_vehicle_size(self):
        return self.vehicle_size
   
class Eco(Vehicle):
    '''        
    Length < 4.5m
    '''
    def __init__(self):
        super().__init__(1)

class Limo(Vehicle):
    ''' 
    4.5m < Length < 6m
    '''
    def __init__(self):
        super().__init__(2)

class Van(Vehicle):
    ''' 
    6m < Length < 8m
    '''
    def __init__(self):
        super().__init__(3)


class Driver:
    def __init__(self, id, vehicle):
        '''
        id: identify every unique drivers in the parking system
        vehicle: vehicle type
        payment_due: how much should this driver pay
        '''
        self._id = id
        self._vehicle = vehicle
        self._payment_due = 0

    def get_vehicle(self):
        return self._vehicle

    def get_id(self):
        return self._id

    def charge(self, amount):
        self._payment_due += amount