from parking_system import *
from parking_floor import *
from parking_garage import *

# Test examples
parkingGarage = ParkingGarage(3, 2)
parkingSystem = ParkingSystem(parkingGarage, 5)

driver1 = Driver(1, Eco())
driver2 = Driver(2, Limo())
driver3 = Driver(3, Van())

print(parkingSystem.park_vehicle(driver1))      # true
print(parkingSystem.park_vehicle(driver2))      # true
print(parkingSystem.park_vehicle(driver3))      # false

print(parkingSystem.remove_vehicle(driver1))    # true
print(parkingSystem.remove_vehicle(driver2))    # true
print(parkingSystem.remove_vehicle(driver3))    # false
