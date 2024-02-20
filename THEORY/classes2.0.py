class Car:
    def __init__(self, brand, speed=0):
        self.car_brand = brand
        self.speed = speed

    def set_speed(self, speed):
        self.speed = speed

class Ferrari(Car): #Ferrrari es una nueva clase que proviene(inheritance) de Car(mother class), por lo que tiene todas sus atributos y variables
    pass


mycar = Car("Renault")
yourcar = Ferrari("Ferrari") #hay q poner "Ferrari" porq es la brand y esta requirido especificarlo
print(yourcar.car_brand)
yourcar.set_speed(120)
print(yourcar.speed)