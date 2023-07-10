#REGULAR EXPRESSION     (regualr expression is a declarative mechanism to represent a group of strings according to paticular format)
                    #important  applications of regular expressions are:
                    #1>>to devolop validation framework or validation logic
                    #2>>to devolop pattern matching applications
                    #3>>to devolop translators like compilers and interpretors
                    #4>>to devolop digital circuits
                    #5>>to devolop communication protocols like TCP/IP and UDP

import  re
count = 0
pattern = re.compile('ab')
matcher = pattern.finditer("abaababa")
for match in matcher:
    count += 1
    print(match.start(), "...", match.end(), "...", match.group())

print('the no of occurances are', count)


#pass pattern directly as an arguement
import re
count = 0
matcherr = re.finditer("ab", "abaababa")
for match in matcherr:
    count += 1
    print(match.start(), "...", match.end(), "...", match.group())
print('the no of occurances are', count)


#charecter classes
      #[A-Z]
import  re
count = 0
matcher = re.finditer('[A-Z]', 'ACKADFJL2384798243LAJ1843')
for match in matcher:
    count += 1
    print(match.start(), "...", match.end())

print('the total count is:', count)

       #[a-z]
import  re
count = 0
matcher = re.finditer('[a-z]', 'ACKJAlskdnlmvDFJsdclL23ds,/lksjl84798243LAJ1843')
for match in matcher:
    count += 1
    print(match.start(), "...", match.end())

print('the total count is:', count)

           #[0-9]
import  re
count = 0
matcher = re.finditer('[0-9]', 'ACKJAlskdnlmvDFJsdclL23ds,/lksjl84798243LAJ1843')
for match in matcher:
    count += 1
    print(match.start(), "...", match.end())

print('the total count is:', count)

       #[a-zA-Z0-9]
import  re
count = 0
matcher = re.finditer('[a-zA-Z0-9]', 'ACKJAlskdnlmvDFJsdclL23ds,/lksjl84798243LAJ1843')
for match in matcher:
    count += 1
    print(match.start(), "...", match.end())

print('the total count is:', count)


#qualifiers
#a  Exactly one 'a'
#a+  Atleast one 'a'
#a*  Any number of a's including zero number
#a?  Atmost one 'a' ie either zero number or one number
#a{m}  Exactly m number of a's
#a{m,n}  Minimum m number of a's and Maximum n number of a's.


#match() function
import  re
s = input("enter the string you need to check")
m = re.match(s, "asdflkgdfkljeroiufv")
if m != None:
    print('the match is available for the given string:')
    print('start index:', m.start(), "....", m.end())
else:
    print('match is not avilable at the begining of the string')


#fullmatch() meathod
import re
s = input('enter the string here:')
m = re.fullmatch(s, 'saikiranreddy')
if m != None:
    print('the given string is a full match')
else:
    print('the entered string is not a match')

#search() meathod
import re
s = input('enter the pattern here')
m = re.search(s, '19562468')
if m != None:
    print('the given pattern is a match')
    print('the starting index is:', m.start(), ".....", "the end of the match", m.end())
else:
    print('the match is not found')

#findall() meathod
import re
l = re.findall("[0-9]", "a7b9c5kz")
print(l)

#finditer() meathod
import re
l = re.finditer("[a-z]", "a7b9c5kz")
for m in l:
    print(m.start(), "....", m.end(), ".....", m.group())

#sub()   {substitution or replacement}
#[syntax : re.sub(regex,replacement,targetstring)]
import re
r = re.sub("[0-9]", "*", "asd87asfd978adf79afs9")
print(r)


#subn()  meathod
import re
r = re.subn("[0-9]", "*", "asd87asfd978adf79afs9")
print(r)
print('the result string', r[0])
print('the no of occurances', r[1])

#split() meathod
import re
r = re.split(".", "sai.kiran.reddy.19.56.24.68")
print(r)
for t in r:
    print(r)

#^symbol meathod    (check weather the provided string starts wth our pattern or not)
import re
s = input('enter the string here')
m = re.search("^learn", s)
if m!= None:
    print("yes!!!!  the string starts with our provided pattern")
else:
    print('no!!!! it does not match our pattern')

#$symbol (to check if the provided string end with our pattern or not)

import re
s = input('enter the string here')
m = re.search("learn$", s)
if m!= None:
    print("yes!!!!  the string ends with our provided pattern")
else:
    print('no!!!! it does not match our pattern')


#IGNORECASE meathod

import re
s = input('enter the string here')
m = re.search("learn$", s, re.IGNORECASE)
if m!= None:
    print("yes!!!!  the string ends with our provided pattern")
else:
    print('no!!!! it does not match our pattern')


#regular expression to represent all java language identifiers
import re
s = input('eenter the string here')
d = re.fullmatch('[a-k][0369][a-zA-Z0-9#]*', s)
if d != None:
    print("the entered string is not a full match")
else:
    print('it is not a full match')

#regular expression to represent all ten digits of a mobile number
import re
s = input('eenter the mobile number  here')
n = re.fullmatch('[0-9]{10}', s)
if d != None:
    print("the entered string is not a full match")
else:
    print('it is not a full match')


#web screaping using regular expression
import re, urllib
import urllib.request
sites = "google rediff".split()
print(sites)
for s in sites:
    print('searching....', s)
    u = urllib.request.urlopen("http://" +s+ ".com")
    text = u.read()
    title = re.findall("<title>.*</title>", str(text),re.L)
    print(title[0])

#program to get all phone numbers in redbus.in by suing webscraping and regula expressions
import re, urllib
import urllib.request
u = urllib.request.urlopen("https://www.redbus.in/info/contactus")
text = u.read()
numbers = re.findall("[0-9-]{7}[0-9-]+", str(text), re.L)
for n in numbers:
    print(n)


#check wether the given mail id is valid or not
import re
s = input("enter the mail id:")
m = re.fullmatch("\w[a-zA-Z0-9_.]*@gmail[.]com", s)
if m != None:
    print('valid email id')
else:
    print('invalid email id')



# check wether the given car registration number is valid telangana state carnumber or not
    import re

    s = input("enter the car registration number")
    m = re.fullmatch("TS[012][0-9][A-Z]{2}\d{4}", s)
    if m != None:
        print('valid veichle registration number')
    else:
        print('invalid veichle registration number')