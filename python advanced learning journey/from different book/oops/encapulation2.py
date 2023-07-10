class saik():
    def __init__(self):
        self.course = "machine learning code"
        self.__tech ="python"

    def course(self):
        return self.course + "   :   " + self.__tech

    def set__tech(self, x):
        self.__tech = x

    def get__tech(self):
        return self.__tech

ob = saik()
ob.set__tech("sakiran g")
ob.course()
ob.get__tech()