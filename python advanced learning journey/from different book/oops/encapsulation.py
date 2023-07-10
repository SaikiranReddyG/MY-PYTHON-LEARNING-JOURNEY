#wrapping up of data under a sheild ex capsule tablets
class saik():
    def __init__(self):
        self.course = "python programming course"
        self.__tech = "python"                       #"__" is used as encapulation for "tech"

    def courseName(self):
        return self.course +self.__tech


ob = saik()

print(ob.course)
print(ob._saik__tech)
print(ob.courseName())


