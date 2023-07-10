class person(object) :
    def __init__(self,name ,age ,gender):
        self.name = name     #public acess modifier
        self._age = age      #protected acess modifier
        self.__gender = gender #private acess modifier


class employee(person):
    def __init__(self, name, age, gender, eid):
        super(employee,self).__init__(name, age, gender)
        self.eid = eid

    def print_gender(self):
        print('gender of the employee is', self.__gender)


    def print_age(self):
       print('age of employee is', self._age)


    #def print_gender(self):
        #print('gender of the employee is', self.__gender)

e1 = employee('saikiran', 31, 'male', 1)
print(e1.name)
e1.print_age()
e1.print_gender()