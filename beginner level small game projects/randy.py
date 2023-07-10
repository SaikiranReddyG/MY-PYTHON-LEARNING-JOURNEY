import random
start = 0
end = 1
r = random.Random()
for i in range(20):
    x = [r.randint(start, end)]
    result = '\n'.join(str(num) for num in x)
    print(result)