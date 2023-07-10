#for loop                 (if we want to execute some action for every element present in some sequence)
                                 #program to index numbers for letters
s = input('enter some string')
i = 0
for x in s:
    print('the charecter present in string', i ,'index is', x)
    i +=1
                           #program to multiply th given string
for x in range(5):
    print('sai')

                     #program to print first 20 odd numbers
for x in range(21):
    if (x%2!=0):
        print(x)

                      #program to print sum of numbers in the list
list = eval(input('enter the list:'))
sum = 0
for x in list:
    sum = sum + x
    print('the sum=',sum)

#while loop                      #if we want to execute a group of statments iteratively until some condition is false
x = 1                      #to print numbers from 1 to 10
while x >= 10:
    print(x)
    x = x+1

                              #to print the sum of first n numbers
n = int(input('enter a number'))
sum = 0
i = 1
while i<=10:
    sum = sum+1
    i = i+1
    print('sum of first', n, 'numbers is:',sum)


enter_name = ""                #program to print specific name
while enter_name != "sai":
      enter_name = input('enter another name')
print("thanks for conformation")

#Repeat code for every item in sequence  for loop         #Repeat code as long as condition is true  while loop




#infinite loops                      #
i = 0
while True:
    i = i + 1
    print('hiii')

#nested loops

for i in range (4):
    for j in range (4):
        print('i =',i,'j =',j)


#program to display *'s in differnt figures

             #right angled form
n = int(input('enter a number'))
for i in range (1,n+1):
    for j in range(1,i+1):
        print('*',end="")
    print()

         #right angled form2
n = int(input('enter a number'))
for i in range (1,n+1):
    print('*'*i)

          #pyramid style
n = int(input('enter a number'))
for i in range (1,n+1):
    print(" " * (n - i), end="")
    print('*' * i)


