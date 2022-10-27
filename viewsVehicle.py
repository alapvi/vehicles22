from controllervehicle import ControllerVehicle 
from vehicleapi import getDistance
controller = ControllerVehicle()

def readPlate():
    plate=""
    while True:
        plate = input("Enter the plate")
        if (len(plate) == 7):
            numPart = plate[0:4]
            lettersPart = plate[4:]
            if (numPart.isdigit()):
                if (lettersPart.isalpha()):
                    break
        print("Error entering the Plate!!!")
    
    return plate



def addVehicle():
    plate = readPlate()
    desc = input("Enter Description:")
    while True:
        chasis = input("Enter Chasis (17 characters):")
        if (len(chasis) == 17):
            break
        print("Error entering the chasis (17 chaaractes!")
    driver = input("Enter the driver Name:")
    if (controller.addVehicle(plate,desc,chasis,driver)):
        print("Vehicle add successfully!!")
    else:
        print("Error adding the vehicle. Plate already exists!!")

def delVehicle():
    plate= readPlate()
    if (controller.delVehicle(plate)):
        print("Vehicle deleted!!!")
    else: 
        print("Error deleting Vehicle!")


def listVehicles():
    vehicles = controller.getVehicles()
    for plate,vehicle in vehicles.items():
        print("Plate:",plate)
        print("Description:",vehicle.getDesc())
        print("Chasis:",vehicle.getChasis())
        print("Driver:",vehicle.getDriver())
        print("Unconfirmed odometer:")
        for date,odometer in vehicle.getOdometer().items():
            print("\t",date,odometer[0],odometer[1],odometer[2])


def addOdometer():
    plate= readPlate()
    date=input("Enter date [dd/mm/yyyy]:")
    fromcity = input("From:")
    destcity = input("To:")
    kms = getDistance(fromcity,destcity)/1000
    if (controller.addOdometer(plate,date,fromcity,destcity,kms)):
        print("Odometer added successfully!!")
    else:
        print("Error adding odometer!!")

def confirmOdometer():
    plate= readPlate()
    date=input("Enter date [dd/mm/yyyy]:")
    if (controller.confirmOdometer(plate,date)):
        print("Odometer confirmed!!")
    else:
        print("Error confirming odometer!!!")

while True:
    print("Currently there are,", controller.getNumberOfVehicles(), "vehicles registered!")
    print("1.- Add a vehicle")
    print("2.- Delete vehicle")
    print("3.- Add odometer")
    print("4.- Confirm odometer")
    print("5.- List vehicle")
    print("6.- Exit")
    option = int(input("Choose option:"))
    if (option == 6):
        print("Bye!")
        break
    elif (option==1):
        addVehicle()
    elif (option==2):
        delVehicle()
    elif (option==3):
        addOdometer()
    elif (option==4):
        confirmOdometer()
    elif (option==5):
        listVehicles()
    
    
    else:
        print("Option error!!!")