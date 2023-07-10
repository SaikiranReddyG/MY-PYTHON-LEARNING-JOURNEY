class saik():
    def __init__(self):
        self.course = "python programming course"
        self.__tech = "python"

    def courseName(self):
        return self.course + self.__tech

    def get__tech(self):               #get meathod used for encapulation
        return self.__tech

    def set__tech(self,t):             #set meathod is used for encapulation
        self.__tech == t



ob = saik()
ob.set__tech("machine learning")
ob.get__tech()
print(ob.course)
print(ob._saik__tech)
print(ob.courseName())

