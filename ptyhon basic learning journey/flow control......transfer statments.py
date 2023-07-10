#transfer statments

#break             #used inside loops to break loops under some condition

for i in range (20):
    if i==15:
        print('it is enough brake now')
        break
    print(i)

cart=[10,20,600,60,70]
for i in cart:
    if i>500:
        print('buy something less costly')
        break
    print(i)


#continue           #used to skip current iteration and continue to next iteration

for i in range (99):
    if i%2 ==0:
        continue
    print(i)


cart=[10,20,600,60,70]
for i in cart:
    if i>500:
        print('buy something less costly than',i)
        continue
    print(i)

numbers=[10,20,0,5,0,30]
for i in numbers:
    if i == 0:
        print("cannot divide zero")
    print('100/{} = {}'.format(i,100/i))


         #using else statment with break

cart=[10,20,30,40,50]
for i in cart:
    if i >= 500:
        print('buy something less costly')
        break
    print(i)
else :
        print('you have bought everything')


                        #Q) How to exit from the loop? By using break statement
                        #Q)How to skip some iterations inside loop? By using continue statement.
                        #Q)When else part will be executed wrt loops? If loop executed without break


#pass statment
for i in range (99):
    if i%9==0:
        print(i)
else:
    pass