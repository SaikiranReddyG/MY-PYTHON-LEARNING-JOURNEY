#STRING

# defination >>>((any sequence of charecters in single or double quotes is considered as a string))

#multiline string  >>>((it is defined by triple single or double quotes))

#accesing charecters in a string by
        # 1>index
s = 'saikiranreddy'
print(s[0])
print(s[5])
print(s[9])

         #program to display charecters of a string index wise  (positive and negitive)
k = input("enter any string")
i = 0
for x in k:
        print('the charecters at positive index{} and at negetive index{} is {}'.format(i,i-len(k),x))
        i += 1

        #2>slice operator
        #syntax    =    string_name[begining_index:ending_index:step_size]
f = "saikiranreddy"
print(f[2:5:1])
print(f[:5:1])
print(f[2::1])
print(f[2:5:])
print(f[::1])
print(f[::-1])
print(f[::-2])


#mathematical operations on a string

         #1> +
a = 'sai'+'kiran'
print(a)

          #2> *
a = 'sai'*3
print(a)

#to find length of a string
d = 'saikiranreddy'
print(len(d))

                    #program to access each charecter of a string in forward and backward direction by using while loop
g = 'gnagula'
n = len(g)
i = 0
print('forward direction')
while  i<n:
    print(g[i],end='  ')
    i = i+1
print('backward direction')
i = -1
while  i >= -n:
    print(g[i],end='  ')
    i = i-1

                                  #alternative way
g = input('enter a string')
print('forward direction')
for i in g:
    print(i,end=' ')
print('forward direction')
for i in g[::]:
    print(i,end=' ')
print('backward direction')
for i in g[::-1]:
    print(i,end=' ')

                   #checking membership between two strings
s = input('enter a string')
f = input('enter another string')
if f in s:
    print(f,'is present in s')
else:
    print(f,'is not present in s')

                  #comparision of strings (< > >= <= == !=)         #comparision is done based on alphabetical order
s = input('enter 1st string')
f = input('enter 2nd string')
if s>f:
    print('s is greater')
elif s<f:
    print('f is greater')
elif s==f:
    print('both are equal')
else:
    print('both are not in the same format')

       #finding sub strings
#find()
s = "sai kiran reddy"
print(s.find("kiran"))

#index()
e = input('enter 1st string')
t = input('eneter2nd string')
try:
    t.index(e)
except ValueError:
    print('try another string')
else:
    print('its found')

#counting substrings
v ="abcabcabcabcadda"
print(v.count('c'))

#replacing strings
d = 'learing python is very hard'
e = d.replace("hard","easy")
print(e)

s = "ababababababab"
d = s.replace('a','z')
print(d)

#splitting of a string      # syntax = s.split(seperator)
s = input('enter a string')
i =s.split()
for x in i:
    print(x)

s="22-02-2018"
d = s.split("-")
for x in d:
     print(x)

#joining of strings           syntax = seperator.join(group of strings)
w = 'sai' 'kiran' 'reddy'
e = '_'.join(w)
print(e)

#changing case of string chatrecters
a = 'gangula sai kiran reddy'
print(a.upper())
print(a.lower())
print(a.swapcase())
print(a.capitalize())
print(a.title())

#hecking type of charecters of a string
a = 'gangula sai kiran reddy'
print(a.isalnum())
print(a.isalpha())
print(a.isdigit())
print(a.isdecimal())
print(a.isupper())
print(a.islower())
print(a.istitle())
print(a.isspace())


i = input('enterany charecter')
if i.isalnum():
    print('its a number')
if i.isalpha():
    print('it is alphabet')
elif i.isupper():
    print('its uppercase')
elif i.isdigit():
    print('it is a digit')
elif i.isspace():
    print('its just spaces')
else:
    print('enter another charecter')


#FORMATTING STRINGS      #(we can formst strings by using replacement operator{} and format() meathod)
collage = "gnu_university"
course = "ECE"
year = "4th"
joining = 2020
ending = 2023
print('collage {} and course {} and year {} and joining {} and ending {}'.format(collage,course,year,joining,ending))



