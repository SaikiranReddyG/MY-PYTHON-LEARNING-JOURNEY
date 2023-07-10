n = 5
   # pattern of a square
for i in range(n) :
    for j in range(n) :
        print('*',end=' ')
    print()
   #for patter of right angle triangle
for i in range (n) :
    for j in range(i + 1) :
        print('*',end=' ')
        print()
   #for pattern of reverse right angle triangle
for i in range (n) :
    for j in range(i , n) :
        print('*',end=' ')
        print()
    #for pattern of a inc and dec right angle triangle
for i in range (n) :
    for j in range(i , n) :
        print(' ',end=' ')
    for j in range(i+1):
        print('*',end=' ')
        print()
    #for pattern of a inc and dec right angle triangle
for i in range (n) :
    for j in range(i + n) :
        print(' ',end=' ')
    for j in range(i , n):
        print('*',end=' ')
        print()
 #for pattern of a inc and dec right angle triangle
for i in range (n) :
    for j in range(i , n) :
        print(' ',end=' ')
    for j in range(i):
        print('*',end=' ')
    for j in range (i+1):
        print('*',end=' ')
        print()