class Car:
    def __init__(self, brand, speed=0): #paratemeter of all methods, is the object it self
        self.brand = brand # self . algo is an atribute (variable atach to the object)
        self.speed = speed
#brand es "Renault" o "Ferrari", y haciendo eso haces que la marca de coche (ese string) sea un atributo del objeto
    def set_speed(self, speed):
        self.speed = speed

    def get_speed(self):
        return self.speed

    def get_brand_nationality(self):
        if self.brand == "Renault":
            return "France"
        if self.brand == "Ferrari":
            return "Italy"

    #def speed(self):
        #return 100
mycar = Car("Renault", 30) # this is a obtect#if Car is not there init would be empty
print(mycar.get_speed())
mycar.set_speed(80)
print(mycar.speed)

print(mycar.get_brand_nationality())

yourcar = Car("Ferrari", 250)
print(yourcar.speed)#this and the line bellow are equivalent, this one is the prefer way
print(yourcar.get_speed())