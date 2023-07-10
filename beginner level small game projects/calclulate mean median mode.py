"""program to calculate mean median and mode of given input numbers"""


def mean(numbers):
    return sum(numbers) / len(numbers)

def median(numbers):
    n = len(numbers)
    sorted_num = sorted(numbers)
    if n % 2 == 0:
        return sorted_num[n//2-1] + sorted_num[n//2] / 2
    else:
        return sorted_num[n//2]


def mode(numbers):
    counts = {}
    for num in numbers:
        if num in counts:
            counts[num] += 1

        else:
            counts[num] = 1

    max_count = max(counts.values())
    modes = [num for num, count in counts.items() if count == max_count]

    return modes[0]


numbers = [2,3,4,4,5,6,6,7,8,9,99,8,999]
n = numbers
print('mean of the numbers is: ', mean(n))
print('median of the numbers is: ', median(n))
print('mode of the numbers is: ', mode(n))
