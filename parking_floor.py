from vehicles import *

# 2
class ParkingFloor:
    '''
    This class represents a floor in the parking garage and is responsible for managing the parking spots on that floor.
    '''
    def __init__(self, spot_count):
        '''
        _spots: a list representing the availability of each spot on the floor, zero means spots are vacant.
        _vehicle_map: a dictionary mapping vehicles to their parking spot range on the floor
        '''
        self._spots = [0] * spot_count          # 车位数
        self._vehicle_map = {}      # 每一辆车的停泊范围

    def park_vehicle(self, vehicle):
        '''
        park a vehicle on this floor
        '''
        size = vehicle.get_vehicle_size()
        l, r = 0, 0     # set 2 scope pointers for searching a parking spot
        while r < len(self._spots):
            if self._spots[r] != 0:
                l = r + 1
            if r - l + 1 == size:
                # we found enough spots, park the vehicle
                for k in range(l, r+1):
                    self._spots[k] = 1
                self._vehicle_map[vehicle] = [l, r]
                return True
            
            r += 1
        return False

    def remove_vehicle(self, vehicle):
        '''
        remove a vehicle from the floor
        '''
        start, end = self._vehicle_map[vehicle]
        for i in range(start, end + 1):
            self._spots[i] = 0      # change 1 to 0
        del self._vehicle_map[vehicle]

    def get_parking_spots(self):
        '''
        returns the current availability of parking spots on the floor.        
        '''
        return self._spots

    def get_vehicle_spots(self, vehicle):
        '''
        returns the spot range occupied by a specific vehicle
        '''
        return self._vehicle_map.get(vehicle)
