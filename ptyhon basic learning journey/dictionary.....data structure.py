#DICTIONARY           (represent agroup of objects as key value pairs)
# (duplicates of keys are not allowed but values allowed)
# (mutable)
# (insertion order not preserved)
# (indexing and slicing not applicable)

d = {}
print(type(d))
d[1] = 'sai'
d[2] = 'kiran'
d[3] = 'reddy'
print(d)

#accessing data in dictionary using keys
name = {1: 'sai', 2: 'kiran', 3: 'reddy'}
print(name[1])
print(name[2])

#program to enter names and marks percentage of students
rec = {}
n = int(input('enter the number of students: '))
i = 1
while i<=n:
    name = input('student name:')
    marks = input('enter the marks % of the student:')
    rec[name] = marks
    i = i+1
print('student name:',"\t",'% of marks')
for x in rec:
    print("\t",x,"\t\t",rec[x])


#update of dictionaries
saik = {1: 'sai', 2: 'kiran', 3: 'reddy'}
print(saik)
saik[4] = "gangula"
saik[5] = "saikiran"
saik[6] = "reddy"
print(saik)

#deleting of elements of dictionary
red = {1: 'sai', 2: 'kiran', 3: 'reddy', 4: 'gangula', 5: 'saikiran', 6: 'reddy'}
del red[1]
del red[5]
print(red)

#clear()
ed = {1: 'sai', 2: 'kiran', 3: 'reddy', 4: 'gangula', 5: 'saikiran', 6: 'reddy'}
ed.clear()
print(ed)

#del d
e = {1: 'sai', 2: 'kiran', 3: 'reddy', 4: 'gangula', 5: 'saikiran', 6: 'reddy'}
del e
print(d)


#functions of dictionary
#dict()
f = dict([(32,'dfa'),(432,'daf'),(43,'fws'),(64,'sdf')])
print(f)


u = {1: 'sai', 2: 'kiran', 3: 'reddy', 4: 'gangula', 5: 'saikiran', 6: 'reddy'}
#len()
print(len(u))
#keys()
print(u.keys())
#values()
print(u.values())
#items()
print(u.items())
#copy()
d1 = u.copy()
print(d1)
#setdefault()
u.setdefault(99,"reddie")
#update()
d2 = {}
d2.update(d1)
print(d2)
#get()
print(u.get(5))
#pop()
print(u.pop(2))
#clear()
u.clear()
print(u)

#program to print sum of values of a dictionary
d = dict(eval(input('enter the dictionaty')))
s = sum(d.values())
print('sum=',s)


#program to find no of occurances of letters in a give string
word = input('enter a word:')
d = {}
for x in word:
    d[x] = d.get(x,0)+1
for k,v in d.items():
    print(k,'occured',v,'times')

#chatgpt way
stringg = input('enter a string:')
letter_count = {}
for char in stringg:
    if char.isalpha():
        char + char.lower()
        if char in letter_count:
            letter_count[char]  += 1
        else:
            letter_count[char] = 1
for letter,count in letter_count.items():
    print(f"{letter}: {count}")


#program to find no of vowels in a given string
word = input('enter a word:')
vowels = {'a','e','i','o','u'}
d = {}
for x in word:
    if x in vowels:
        d[x] = d.get(x,0)+1
for k,v in sorted(d.items()):
    print(k,'occured',v,'times')

#program toaccept student name and marks as input nad create a dictionary aalso display marks by taking name as input
n = int(input('enter the no students:'))
d ={}
for i in range (n):
    name = input('enter the name of the student:')
    marks = input('enter the marks of the student:')
    d[name] = marks
while True:
    name = input('enter student name to get marks:')
    marks = d.get(name,-1)
    if marks==-1:
        print('student not found!!!')
    else :
        print('the marks of',name,'are',marks)
print('thanks for using our application')



