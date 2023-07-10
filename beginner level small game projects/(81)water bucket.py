import sys
print('water bucket puzzle by saikiran reddy')
GOAL = 4
"""the exact amount of water to have in a bucket to win"""
steps = 0
"""keep track of how many steps the player made to solve this"""

# the amount of water in each bucket
water_in_bucket = {'8': 0, '5': 0, '3': 0}

while True:
    # display the current state of the buckets
    print()
    print('try to get' + str(GOAL) + 'L of water into one of these buckets')

    water_display = []
    """contains string of water or empty space"""

    # get the string for the 8L bucket
    for i in range(1, 9):
        if water_in_bucket['8'] < i:
            water_display.append('      ')  # add empty space
        else:
            water_display.append('WWWWWW')  # add water

    # get the string for the 5L bucket
    for i in range(1, 6):
        if water_in_bucket['5'] < i:
            water_display.append('      ')  # add empty space
        else:
            water_display.append('WWWWWW')  # add water

    # get the string for the 3L bucket
    for i in range(1, 4):
        if water_in_bucket['3'] < i:
            water_display.append('      ')  # add empty space
        else:
            water_display.append('WWWWWW')  # add water

    # display the buckets with the amount of water in each of them
    print('''
8|{7}|
7|{6}|
6|{5}|
5|{4}|  5|{12}|
4|{3}|  4|{11}|
3|{2}|  3|{10}|  3|{15}|
2|{1}|  2|{9}|  2|{14}|
1|{0}|  1|{8}|  1|{13}|
 +------+   +------+   +------+
    8L         5L         3L
'''.format(*water_display))

    # check if any of the bucket has goal amount of water:
    for water_amount in water_in_bucket.values():
        if water_amount == GOAL:
            print('GOOD JOB you have solved it!!!!!!!!!!!', steps, 'steps!!')

    # let the player select an action to do with the bucket
    print('you can:')
    print('   (F)ill the bucket')
    print('   (E)mpty the bucket')
    print('   (P)our one bucket into another')
    print('   (Q)uit')

    while True:  # keep asking until the player enters a valid action
        move = input('> ').upper()
        if move == 'QUIT' or move == 'Q':
            print('thanks for playing !!!!!!!!!')
            sys.exit()

        if move in ('F', 'E', 'P'):
            break  # player has selected a valid selection

        print('enter F, E, P, or Q')

    # let the player select the bucket
    while True:
        print('select a bucket 8,5,3 or Quit:')
        srcBucket = input('> ').upper()

        if srcBucket == 'QUIT':
            print('thanks for playing!!!!')
            sys.exit()

        if srcBucket in ('8', '5', '3'):
            break  # player has selected a valid bucket

    # carry out selected action
    if move == 'F':
        # set the amount of water to the max size
        srcBucketSize = int(srcBucket)
        water_in_bucket[srcBucket] = srcBucketSize
        steps += 1

    elif move == 'E':
        water_in_bucket[srcBucket] = 0   # set water amount to nothing
        steps += 1

    elif move == 'P':
        # let the player select a bucket to pour into
        while True:  # keep asking until valid bucket entered
            print('select a bucket to pour into: 8, 5, or 3')
            dst_bucket = input('> ').upper()
            if dst_bucket in ('8', '5', '3'):
                break   # player has selected a valid bucket

        # figure out the amount to pour
        dst_bucket_size = int(dst_bucket)
        empty_space_in_dst_bucket = dst_bucket_size - water_in_bucket[dst_bucket]
        water_in_src_bucket = water_in_bucket[srcBucket]
        amount_to_pour = min(empty_space_in_dst_bucket, water_in_src_bucket)

        # pour out from this bucket
        water_in_bucket[srcBucket] -= amount_to_pour

        # put the poured out water into other bucket
        water_in_bucket[dst_bucket] += amount_to_pour
        steps += 1

    elif move == 'C':
        pass  # if the player selected cancel do nothing








