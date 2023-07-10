from threading import *
class demo:
    def show(self):
        for i in range(5):
            print("this is a child class")
obj = demo()
t = Thread(target=obj.show())
for i in range(5):
    print("this is a parent thread")
