from threading import *
def show():
    print("this is a child thread")
t = Thread(target = show())
t.start()
print ("this is parent thread")
