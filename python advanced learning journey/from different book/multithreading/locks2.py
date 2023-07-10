import time
import multiprocessing
import locks

def add_500_lock(total, lock):
    for i in range(100):
       time.sleep(0.01)
       lock.acquire()
       total.value += 5
       lock.release()


def sub_500_lock(total,  lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        total.value -= 5
        lock.release()


if __name__ == '__main__':

    total = value()
    lock = locks()
    add_prcess = multiprocessing(target=add_500_lock, args=(total, lock))
    sub_prcess = multiprocessing(target=sub_500_lock, args=(total,  lock))
    add_prcess.start()
    sub_prcess.start()

    add_prcess.join()
    sub_prcess.join()
    print(total.value)