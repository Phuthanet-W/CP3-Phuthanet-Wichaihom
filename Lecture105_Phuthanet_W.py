class Vehicle:
    LicenseNo = ""
    SerialNo = ""
    color = ""
    def turnOnAir(self):
        print(self.color,">> Trun on :Air",)

class car(Vehicle):
    color = ""

class pickup(Vehicle):
    color = " "

class Van(Vehicle):
    color = " "

class estatecar(Vehicle):
    color = " "

car1 = car()
car1.color = "Red car"
car1.turnOnAir()
pickup1 = pickup()
pickup1.color = "Green pickup"
pickup1.turnOnAir()
van1 =Van()
van1.color = "Blue van"
van1.turnOnAir()
estatecar1 = estatecar()
estatecar1.color = "Pink estatecar"
estatecar1.turnOnAir()