from threading import *
class Mythread(Thread):
    def run(self):
        for i in range(5):
            print ("this is a child class")
t = Mythread()
t.start()
for i in range(5):
    print ("\nthis is a main thread")
