class Vehicle:
    def __init__(self,plate,desc,chasis,driverName):
        self.__plate = plate
        self.__desc = desc
        self.__chasis = chasis
        self.__driverName = driverName
        self.__odometer = {}
        self.__totalKms = 0
        self.__history = ""
    
    def getPlate(self):
        return self.__plate

    def getDesc(self):
        return self.__desc

    def getChasis(self):
        return self.__chasis
    
    def getDriver(self):
        return self.__driverName
    
    def getOdometer(self):
        return self.__odometer
    
    def getKilometers(self):
        return self.__totalKms

    def getHistory(self):
        return self.__history
    
    def addOdometer(self,date,fromcity,tocity,kms):
        self.__odometer[date] = (fromcity,tocity,kms)
    
    def confirmOdometer(self,date):
        detailsOdo = self.__odometer.pop(date)
        self.__history += str(detailsOdo[0]) + "-" + str(detailsOdo[1]) +"-" + str(detailsOdo[2]) +"\n"
        self.__totalKms += detailsOdo[2]

