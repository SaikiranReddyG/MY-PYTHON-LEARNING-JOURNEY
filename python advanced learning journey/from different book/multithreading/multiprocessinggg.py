import multiprocessinggg
import time
import math

results_a = []
results_b = []
results_c = []

def make_claculations_one(numbers):
    for number in numbers:
        results_a.append(math.sqrt(number **  3))

def make_claculations_two(numbers):
    for number in numbers:
        results_b.append(math.sqrt(number **  4))


def make_claculations_three(numbers):
    for number in numbers:
        results_c.append(math.sqrt(number **  5))




if __name__ == '__main__':

    number_list = list(range(100000))


    p1 = multiprocessing(target=make_claculations_one, args=(number_list,))
    p2 = multiprocessing(target=make_claculations_two, args=(number_list,))
    p3 = multiprocessing(target=make_claculations_three, args=(number_list,))
    start = time.time()
    p1.start()
    p2.start()
    p3.start()
    end = time.time()

    print(end - start)

    temp_a = results_a
    temp_b = results_b
    temp_c = results_c

    start = time.time()
    make_claculations_one(number_list)
    make_claculations_two(number_list)
    make_claculations_three(number_list)
    end = time.time()

    print(end-start)
    print(temp_a == results_a)
    print(temp_c == results_c)
    print(temp_b == results_b)