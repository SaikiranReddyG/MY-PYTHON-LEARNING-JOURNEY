class Parent:
    def __init__(self, fname, fage):
        self.name = fname
        self.age = fage
    def view(self):
        print(self.name, self.age)


class Child(Parent):
    def __init__(self, fname, fage):
        Parent.__init__(self, fname, fage)
        self.lastname = "saik"
    def view(self):
        print(self.age, self.lastname, self.name)



ob = Child(23 , "python")
ob.view()