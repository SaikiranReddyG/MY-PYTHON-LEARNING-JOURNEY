class person:

    def __int__(self,n,g,a):
        self.name = n
        self.gender = g
        self.age = a

    def talk(self):
        print('hi iam', self.name)

    def vote(self) :
        if self.age<18 :
            print('not eligible to vote')
        else :
            print('eligible to vote')


obj = person('sam','male','22')
obj2 = person('jessie','female',16)

obj.talk()
obj.vote()

obj2.talk()
obj2.vote()