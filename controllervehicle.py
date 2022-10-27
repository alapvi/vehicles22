from vehicle import Vehicle

class ControllerVehicle():

    def __init__(self):
        self.__vehicles = {}   #Key -> Plate, Value --> Vechicle
    

    def addVehicle(self,plate,desc,chasis,driver):
        if plate in self.__vehicles:
            return False
        
        newVehicle = Vehicle(plate,desc,chasis,driver)
        self.__vehicles[plate] = newVehicle
        return True

    
    
    def delVehicle(self,plate):
        if plate not in self.__vehicles:
            return False

        return self.__vehicles.pop(plate)  # del self.__vehicles[plate]
    
    def getNumberOfVehicles(self):
        return len(self.__vehicles)

    def addOdometer(self,plate,date,fromcity,tocity,kms):
        if plate not in self.__vehicles:
            return False
        vehicle = self.__vehicles[plate]
        vehicle.addOdometer(date,fromcity,tocity,kms)
        return True
    
    def getVehicles(self):
        return self.__vehicles

    def confirmOdometer(self,plate,date):
        if (plate not in self.__vehicles):
            return False
        vehicle = self.__vehicles[plate]
        if date not in vehicle.getOdometer():
            return False
        vehicle.confirmOdometer(date)
        return True    








