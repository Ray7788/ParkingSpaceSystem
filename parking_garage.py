from parking_floor import *

# 3
class ParkingGarage:
    '''
    represents the entire parking garage and is responsible for managing multiple parking floors. 
    '''
    def __init__(self, floor_count, spots_per_floor) -> None:
        '''
        floor_count: floor number 楼层数
        spots_per_floor: how many spots in this floor 车位数
        _parking_floors: a list that holds instances of the ParkingFloor class, representing the different floors in the parking garage.
        '''
        self._parking_floors = [ParkingFloor(spots_per_floor) for _ in range(floor_count)]
        
    def park_vehicle(self, vehicle):
        for floor in self._parking_floors:
            if floor.park_vehicle(vehicle):
                return True
        return False
    
    def remove_vehicle(self, vehicle):
        for floor in self._parking_floors:
            if floor.get_vehicle_spots(vehicle):
                floor.remove_vehicle(vehicle)
                return True
        return False
