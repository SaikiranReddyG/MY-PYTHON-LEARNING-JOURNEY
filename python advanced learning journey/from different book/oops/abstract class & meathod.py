from abc import ABC, abstractmethod

class computer(ABC):
    @abstractmethod
    def process(self):
        pass

class laptop(computer):
    def process(self):
        print("it is running")

class whiteboard(computer):
    def write(self):
        print('it is writing')

class programmer:
    def work(self,com):
        print("solving bugs")
        com.process()

com = computer()
#com1 = laptop()
com2 = whiteboard(com)
#com.process()
prog1 = programmer()
prog1.work(com2)
#com1.process()