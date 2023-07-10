#lists                (insertion order is preservd and duplication are allowed) using index
                      #size can be increased and decreased )
l = list(range(0,100,5))
print(l)
print(type(l))

#accessing elements of a list
     #using index
l = list(range(0,100,5))
print(l[1])
print(l[-3])
print(l[13])

      #using slice operator
n=[1,2,3,4,5,6,7,8,9,10]
print(n[2:5:2])
print(n[:5:2])
print(n[2::2])
print(n[2:5:])
print(n[2:7:2])

#mutability of a list
v=[1,2,3,4,5,6,7,8,9,10]
v[3]= 44
print(v)

#transversing the elements of a list
         #using while loop
c=[1,2,3,4,5,6,7,8,9,10]
i = 0
while i<len(c):
    print(c[i])
    i += 1

       #using for loop
m=[1,2,3,4,5,6,7,8,9,10]
for m1 in m:
    print(m1)

#to display only even numbers
b=[1,2,3,4,5,6,7,8,9,10]
for b1 in b:
    if b1%2==0:
        print(b1)

#to display elements by index wise
j=[1,2,3,4,5,6,7,8,9,10]
x = len(j)
for i in range(x):
    print(j[i],'positive index place is:',i,'negitive index place is:',i-x)

#programs to find about the list
   #len()
o=[1,2,3,4,5,6,7,8,9,10,4,6,23,5,4,4,4,6,8,9]
print(len(o))
print(o.count(4))
print(o.count(6))
print(o.count(1))
print(o.index(4))
print(o.index(6))
print(o.index(1))
print(o.index(8))
print(0 in o)

#manipulating elements of a list
#append()

p=[1,2,3,4,5,6,7,8,9,10,4,6,23,5,4,4,4,6,8,9]
p.append('jndxksa')
p.append('44')
print(p)


      #to make a list of numbers divisible by 10 upto 100
li = []
for i in range (101):
    if i%10 ==0:
        li.append(i)
print(li)

#insert()
p=[1,2,3,4,5,6,7,8,9,10,4,6,23,5,4,4,4,6,8,9]
p.insert(5,'jndxksa')
p.insert(1,'44')
print(p)

#extend()
u=[1,2,3,4,5,6,7,8,9,10,4,6,23,5,4,4,4,6,8,9]
v = [11,22,33,44,55,66,77,88,99]
u.extend(v)
print(u)
w = ['ccuuvv']
u.extend(w)
print(u)

#remove
u=[1,2,3,4,5,6,7,8,9,10,4,6,23,5,4,4,4,6,8,9]
u.remove(10)
u.remove(4)
print(u)

#poop()
u=[1,2,3,4,5,6,7,8,9,10,4,6,23,5,4,4,4,6,8,9]
pu = u.pop()
pi = u.pop(4)
print(pu)
print(pi)
print(u)

#>>>>>append(), insert(), extend()  for increasing the size/growable nature
#>>>>remove(), pop()  for decreasing the size /shrinking nature

#ordering of elements

#reverse
h =[1,2,3,4,5,6,7,8,9,10,4,6,23,5,4,4,4,6,8,9]
h.reverse()
print(h)

#sort
k =[1,2,3,4,5,6,7,8,9,10,4,6,23,5,4,4,4,6,8,9]
f =['h','g','s','t','a','rea','asa']
k.sort()
print(k)
f.sort()
print(f)


#sort in revrese
jf =[1,2,3,4,5,6,7,8,9,10,4,6,23,5,4,4,4,6,8,9]
jf.sort()
print('1st sort=',jf)
jf.sort(reverse=True)
print('2nd sort = ',jf)

#aliasing      (The process of giving another reference variable to the existing list is called aliasing.)
df = [1,2,3,4,5,6,7,8,9,10,4,6,23,5,4,4,4,6,8,9]
rt = df
print('1st df =', df)
print('1st rt =',rt)
rt[2] = 999
print('2nd df =', df)
print('2nd rt =',rt)


#cloning       (The process of creating exactly duplicate independent object is called cloning.)
        #cloning using slice operator
x = [1,2,3,4,5,6,7,8,9,10,4,6,23,5,4,4,4,6,8,9]
y = x[:]
y[1] = 9090
print(x)
print(y)

        #cloning using copy() function
x = [1,2,3,4,5,6,7,8,9,10,4,6,23,5,4,4,4,6,8,9]
y = x.copy()
y[1] = 9090
print(x)
print(y)




#mathematical objects for list
     #1>>concentination (+)
aa = [33,44,55,66]
bb = [77,66,55,44]
c = aa + bb
print(c)

   #2>>repitation operator(*)
aaa = [5,5,5,6]
bbb = aaa*3
print(bbb)

        #3>>>comparision operator
x = ["Dog", "Cat", "Rat"]
y = ["Dog", "Cat", "Rat"]
z = ["DOG", "CAT", "RAT"]
print(x==y)
print(x==z)
print(y==z)

x = [50, 20, 30]
y = [40, 50, 60, 100, 200]
print(x>y)
print(x<y)
print(y>x)
print(y<x)

#membership operator
cc = [40, 50, 60, 100, 200]
print(40 in cc)
print(55 in cc)
print(66 not in cc )

#clear()
cd = [40, 50, 60, 100, 200]
print(cd)
cd.clear()
print(cd)

#nested list  (take one list inside another list.)
do = [40, [50, 60], 100, 200]
print(do[1])

#nested list as matrix
n=[[10,20,30],[40,50,60],[70,80,90]]
print(n)
print('elements in row:')
for r in n:
    print(r)
print('elements in matrix style:')
for i in range (len(n)):
    for j in range (len(n[i])):
        print(n[i][j],end=' ')
    print()



#finding lists based on conditions
s = [x*x for x in range (1,14)] #to find perfect squares
print(s)
v = [2**x for x in range(1,9)]  #to find powers of 2 in given range
print(v)
m = [x for x in s if x%2 == 0]
print(m)

#PROGRAMS TO DISPLAY UNIQUE VOWELS PRESENT IN THE SENTENCE
VOWELS = ['a','e','i','o','u']
input_sentence = input('enter desired sentence here:')
found = []
for letter in input_sentence:
    if letter in VOWELS:
        if letter not in found:
            found.append(letter)
print(found)
print('no of vowels present in:',input_sentence,'is',len(found))



