class car :
    wheels = 4
    def __init__(self):
        self.milage = 55
        self.company = 'BMW'


c1 = car()
c2 = car()
c1.milage = 77
car.wheels = 5
print(c1.company,c1.milage,c1.wheels)
print(c2.company,c2.milage,c2.wheels)