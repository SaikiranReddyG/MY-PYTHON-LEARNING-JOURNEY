def count_steps_to_zero(n):
    steps = 0
    while n != 0:
        if n %2 == 0:
            n //= 2

        else:
            n -= 1
            steps += 1

    return  steps


for i in range(1,50):
    print(count_steps_to_zero(i))
