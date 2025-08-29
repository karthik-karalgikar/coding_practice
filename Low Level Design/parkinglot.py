from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, license_plate):
        self.license_plate = license_plate
        self.spot = None

    @abstractmethod
    def get_type(self):
        pass

class Car(Vehicle):
    def get_type(self):
        return "Car"
    
class Bike(Vehicle):
    def get_type(self):
        return "Bike"
    
class Truck(Vehicle):
    def get_type(self):
        return "Bike"
    
class ParkingSpot:
    def __init__(self, spot_id, spot_type):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.vehicle = None

    def is_available(self):
        return self.vehicle is None
    
    def park(self, vehicle):
        if self.is_available():
            self.vehicle = vehicle
            self.spot_id = self
            return True
        
        return False
    
    def remove(self):
        if self.vehicle:
            self.vehicle.spot = None
            self.vehicle = None

class ParkingLevel:
    def __init__(self, level_id, spots):
        self.level_id = level_id
        self.spots = spots 
    
    def find_spot(self, vehicle_type):
        for spot in self.spots:
            if spot.is_available():
                if vehicle_type == "Car" and spot.spot_type in ["Compact", "Large"]:
                    return spot
                if vehicle_type == "Bike" and spot.spot_type == "Bike":
                    return spot
                if vehicle_type == "Truck" and spot.spot_type == "Large":
                    return spot
        return None
    
class ParkingLot:
    def __init__(self, levels):
        self.levels = levels
    
    def park_vehicle(self, vehicle):
        for level in self.levels:
            spot = level.find_spot(vehicle.get_type())
            if spot:
                spot.park(vehicle)
                print(f"{vehicle.get_type()} parked at Level {level.level_id}, Spot {spot.spot_id}")
                return True
        print("No available spot!")
        return False
    
    def remove_vehicle(self, vehicle):
        if vehicle.spot:
            vehicle.spot.remove()
            print(f"{vehicle.get_type()} {vehicle.license_plate} left the parking.")
        else:
            print("Vehicle not found in parking.")


