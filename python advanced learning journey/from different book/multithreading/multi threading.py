from threading import *
import time
class demo:
    def num(self):
        for i in range(1,6):
            print("the number is ", i)
            time.sleep(1)

    def double(self):
        for i in range(1,6):
            print("th double of the num is", 2*i)
            time.sleep(1)

    def square(self):
        for i in range(1,6):
            print("the square of the number is ", i*i)
            time.sleep(1)


obj = demo()
t1 = Thread(target=obj.num)
t2=Thread(target=obj.double)
t3=Thread(target=obj.square)


t1.start()
time.sleep(0.2)
t2.start()
time.sleep(0.2)
t3.start()
time.sleep(0.2)


t1.join()
t2.join()
t3.join()

print("this is a main thread")

