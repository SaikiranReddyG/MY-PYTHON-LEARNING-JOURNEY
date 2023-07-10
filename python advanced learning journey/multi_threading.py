#program to print name of the current executing thread
import threading
print('current executing thread!!',threading.currentThread().getName())

#creating thread without using any thread

from threading import *
def display():
    for i in range(1,11):
        print('child thread')

t = Thread(target= display())   #creating thread object
t.start()
for i in range(1,11):
    print("main thread")


#creating thread by extending thread class:
from threading import *
class mythread(Thread):
    def run(self):
        for i in range(1,11):
            print('the child class!!!')

t = mythread()
t.start()
for i in range(1,11):
    print('the parent claass!!!')


#creating thread without extending thread class!!
from threading import *
class test:
    def display(self):
        for i in range(10):
            print('chiled class')

obj = test()
t = Thread(target= obj.display())
t.start()
for i in range(10):
    print('main thread!!!')

#with multi threading!!!
from threading import *
import time
def doubles(numbers):
    for i in numbers:
        time.sleep(2)
        print('doubles value is:',2*i)

def squares(numbers):
    for i in numbers:
        time.sleep(3)
        print('squares value is:',i*i)

numbers = [2,4,6,8,9,5,3,1]
begintime = time.time()
t1 = threading.Thread(target= doubles,args= numbers)
t2 = threading.Thread(target= squares, args= numbers)
t1.start()
t2.start()
t1.join()
t2.join()
print('the total time taken is:',time.time() - begintime)

#without multi threading
from threading import *
import time
def doubles(numbers):
    for i in numbers:
        time.sleep(2)
        print('doubles value is:',2*i)

def squares(numbers):
    for i in numbers:
        time.sleep(3)
        print('squares value is:',i*i)

numbers = [2,4,6,8,9,5,3,1]
begintime = time.time()
doubles(numbers)
squares(numbers)
print('the total time taken is:',time.time() - begintime)

#setting and getting name of the thread:
from threading import *
print(current_thread().getName())
current_thread().setName('saikiran reddy')
print(current_thread().getName())
print(current_thread().name)

#thread identification number:
from threading import *
def test():
    print('child thread!!')

t = Thread(target= test)
t.start()
print('the main thread identity is:',current_thread().ident)
print('the main thread identity:',t.ident)

#no of active threads currently running
from threading import *
import time
def display():
    print(current_thread().getName(),'getting started......')
    time.sleep(2)
    print(current_thread().getName(),'ended......')
print('the no of active threads is',active_count())
t1 = Thread(target= display(), name= 'child thread 1')
t2 = Thread(target= display(), name= 'child thread 2')
t3 = Thread(target= display(), name= "child thread 3")
t1.start()
t2.start()
t3.start()
print('the no of active threads are:',active_count())
time.sleep(2)
print('the no of active threads are:',active_count())

#enumerate() function
from threading import *
import time
def display():
    print(current_thread().getName(),'getting started......')
    time.sleep(2)
    print(current_thread().getName(),'ended......')
print('the no of active threads is',active_count())
t1 = Thread(target= display(), name= 'child thread 1')
t2 = Thread(target= display(), name= 'child thread 2')
t3 = Thread(target= display(), name= "child thread 3")
t1.start()
t2.start()
t3.start()
L = enumerate()
for t in L:
    print('thread name:',t.name)
time.sleep(2)
for t in L:
    print('thread name:',t.name)

#isalive() meathod
from threading import *
import time
def display():
    print(current_thread().getName(),'getting started......')
    time.sleep(2)
    print(current_thread().getName(),'ended......')
print('the no of active threads is',active_count())
t1 = Thread(target= display(), name= 'child thread 1')
t2 = Thread(target= display(), name= 'child thread 2')
t1.start()
t2.start()
print(t1.name,'is alive:',t1.isAlive() )
print(t2.name,'is alive:',t2.isAlive() )
time.sleep(3)
print(t1.name,'is alive:',t1.isAlive() )
print(t2.name,'is alive:',t2.isAlive() )

#join() meathod
from threading import *
import time
def display():
    for i in range(10):
        print('sai thread:')
        time.sleep(2)

t = Thread(target= display())
t.start()
t.join()
for i in range(4):
    print('kiran thread:')


#join(seconds) meathod
from threading import *
import time
def display():
    for i in range(10):
        print('sai thread:')
        time.sleep(2)

t = Thread(target= display())
t.start()
t.join(2)
for i in range(4):
    print('kiran thread:')

#deamon threads   (the threads which are running in the background are deamon threads)

from threading import *
print(current_thread().isDaemon())
print(current_thread().daemon)
current_thread().setDaemon(True)


from  threading import *
def job():
    print('child thread!!')

t = Thread(target= job())
print(t.isDaemon())
t.setDaemon(True)
print(t.isDaemon())

#synchronization
from threading import *
import time
def wish(name):
    for i in range(10):
        print('good morning:',end='')
        time.sleep(2)
        print(name)

t1 = Thread(target= wish, args= ('saikiran',))
t2 = Thread(target= wish, args= ('reddy',))
t1.start()
t2.start()    #getting irregular outputs becoz multiple threads are executing simultaneously

#in python we can implement synchronization by using 1>LOCK  2>RLOCK 3>SEMAPHORE

#LOCK()
from threading import *
import time
L = Lock()                   #provide a lock
def wish(name):
    L.acquire()               #asssign the lock to the thread
    for i in range(10):
        print('good morning:',end='')
        time.sleep(2)
        print(name)
        L.release()            #release the lock



t1 = Thread(target= wish, args= ('saikiran',))
t2 = Thread(target= wish, args= ('reddy',))
t1.start()
t2.start()

from threading import *
L = Lock()
print('the main thread is acquiring the lock!!!!!')
L.acquire()
print('the main thread is trying to acquire the lock the lock again')
L.acquire()


#RLOCK()
                                #Traditional Locking mechanism won't work for executing recursive functions.
                                #To overcome this problem, we should go for RLock(Reentrant Lock).


from threading import *
L = RLock()
print('the main thread is acquiring the lock!!!!!')
L.acquire()
print('the main thread is trying to acquire the lock the lock again')
L.acquire()

#synchronization using Rlock()
from threading import *
import time
U = RLock()
def factorial(n):
    U.acquire()
    if n == 0:
        result = 1
    else:
        result = n * factorial(n - 1)

    U.release()
    return result

def result(n):
    print('the factorial of:', n, 'is', factorial(n))

t1 = Thread(target= result, args= (5,))
t2 = Thread(target= result, args= (9,))
t1.start()
t2.start()


#semaphore ()    ☕ Semaphore can be used to limit the access to the shared resources with limited capacity.
                    #☕ Semaphore is advanced Synchronization Mechanism.

                   #(e for every acquire() call counter value will be decremented and for every release() call counter value will be incremented.)



from threading import *
import time
s = Semaphore(2)


def wish(name):
    s.acquire()
    for i in range(10):
        print('good morning', end='')
        time.sleep(2)
        print(name)

    s.release()


t1 = Thread(target=wish, args=('saikiran',))
t2 = Thread(target=wish, args=('gangula',))
t3 = Thread(target=wish, args=('reddy',))
t1.start()
t2.start()
t3.start()



#bounded semaphore          (BounedSemaphore is exactly same as Semaphore except that the number of release()
                            #calls should not exceed the number of acquire() calls,otherwise we will get ValueError: Semaphore released too many times)





#inter thread communication      (s as the part of programming requirement, threads are required to communicate with each other.)




#inter thread communication using event
from threading import *
import time
def producer():
    time.sleep(2)
    print ("producer thread producing items")
    print('producer thread giving notification by setting event')
    event.set()

def consumer():
    print('consumer thread is waiting for updataion')
    event.wait()
    print('consumer thread got notification and consuming items!!!')

event = Event()
t1 = Thread(target= producer)
t2 = Thread(target= consumer)
t1.start()
t2.start()


from threading import *
import time
def trafficpolice():
    while True :
        time.sleep(5)
        print('traffic police giving green signal')
        Event.set()
        time.sleep(10)
        print('traffic police giving red signal')
        Event.clear()

def driver():
    num = 0
    while True:
        print('driver waiting for green signal')
        Event.wait()
        print('traffic signal is green veichles can move')
        while Event.isSet():
            num = num +1
            print('veichle num:', num, 'crossing the signal')
            time.sleep(4)
            print('traffic signal is RED drivers have to wait')


t1 = Thread(target= trafficpolice)
t2 = Thread(target= driver)
t1.start()
t2.start()


#inter thread communication by  condition object   (e Condition object allows one or more threads to wait until notified by another thread)
from threading import *
def consumer(c):
    c.acquire()
    print('THE CONSUMER WAITING FOR UPDATATION')
    c.wait()
    print('CONSUMER GOT NOTIFICATION AND CONSUMING THEIR ITEM')
    c.release()


def producer(c):
    c.acquire()
    print('producer producing items')
    print('producer giving notification')
    c.notify()
    c.release()

c = Condition()
t1 = Thread(target=consumer, args=(c,))
t2 = Thread(target=producer, args= (c,))
t1.start()
t2.start()


from threading import *
import time
import random
List = []


def producer(C):
    while True:
        C.acquire()
        list = random.randint(1, 100)
        print('producer producing items', list)
        List.append(list)
        print("producer notifying about items")
        C.notify()
        C.release()
        time.sleep(5)


def consumer(C):
    while True:
        C.acquire()
        print('consumer waiting for updatation')
        C.wait()
        print("consumer consumed items", List.pop())
        C.release()
        time.sleep(5)


C = Condition()
t1 = Thread(target=consumer, args=(C,))
t2 = Thread(target=producer, args=(C,))
t1.start()
t2.start()


#inter thread communication using Queue (most enhanced Mechanism for interthread communication and to share data between threads.)
                                        #(Queue internally has Condition and that Condition has Lock.Hence whenever
                                        # we are using Queue we are not required to worry about Synchronization.)
                                        #( put(): Put an item into the queue.
                                        #   get(): Remove and return an item from the queue)

from threading import *
import time
import random
import queue
def producer(q):
    while True:
        item = random.randint(1, 100)
        print('the producer producing items', item)
        q.put(item)
        print('producer giving notification')
        time.sleep(5)

def consumer(q):
    while True:
        print("consumer waiting for updatation")
        print('consumer consumed the items:', q.get())
        time.sleep(5)

q = queue.Queue()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))
t1.start()
t2.start()


#types of queue's

#FIFO  QUEUE     (This is Default Behaviour. In which order we put items in the queue, in the same order the items will come out)
import queue
q = queue.Queue()
q.put(22)
q.put(55)
q.put(88)
while not q.empty():
    print(q.get(),end='      ')

#LIFO QUEUE
import queue
q = queue.LifoQueue()
q.put(22)
q.put(55)
q.put(88)
while not q.empty():
    print(q.get(),end='      ')

#priority order
import queue
q = queue.PriorityQueue()
q.put(22)
q.put(55)
q.put(88)
while not q.empty():
    print(q.get(),end='      ')



#practices with usage of lock

