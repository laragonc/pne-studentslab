class Vehicle: #classes upwards is inheritance and downwards is specialization
    def set_speed(self, speed):
        self.speed = speed

class Car(Vehicle):
    def __init__(self, brand, speed=0):
        self.car_brand = brand
        self.speed = speed

class Ferrari(Car):
    def __init__(self): #you have to call the init of the mother class porq si no no se runea el init de la mother class, pero solo algunas cosas como el brand, a little bit of inheritance
        super().__init__("Ferrari", 100) #super()llama a toda la funcion de la mother class
        self.music = "techno"
    def make_cabrio(self):
        self.speed = 20
        self.music = "loud"
        return "wow"


mycar = Car("Renault")
yourcar = Ferrari() #se quita el "Ferrari" porq se ha creado un init
print(yourcar.car_brand)
yourcar.set_speed(120)
print(yourcar.speed)

print(yourcar.make_cabrio(), "and music is", yourcar.music, "and speed is", yourcar.speed)