class computer :
    def __init__(self):
        self.name = 'saikiran'
        self.age = 22
    def update(self):
        self.age = 33

    def compare(self,other) :
         if self.age == other.age :
             return True
         else:
             return False

c1 = computer()
c2 = computer()

if c1.compare (c2) :
    print('they are same')


c1.update()
print(c2.name)
print(c1.name)