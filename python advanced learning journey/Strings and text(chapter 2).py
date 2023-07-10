#(2.1)splitting strings on any of multiple delimeters
"""for more flexibility of split() function we can use re.split()"""
import  re
line = 'asdf fjdk; afed, fjek,asdf, foo'
print(re.split(r'[;,\s]\s*', line))

#(2.2) matching text at the start or end of the string
"""the simple way to check the begining
 or end of the string is using  startswith() or endswith()"""
filename = 'saikiran.txt'
urlname = 'http://www.python.com'
print(filename.startswith('sai'))
print(filename.endswith('text'))
print(urlname.startswith('http'))
print(urlname.endswith('python'))

"""we can also use regular expression as an alternative"""
import re
url = 'http://www.python.com'
print(re.match('http: |https: |ftp:', url))

#(2.3)matching strings using shell wildcare patterns
from fnmatch import fnmatch
print(fnmatch('saikiranreddy', '*reddy'))
print(fnmatch('saikiranREDDY', '*reddy'))


addresses = [
 '5412 N CLARK ST',
 '1060 W ADDISON ST',
 '1039 W GRANVILLE AVE',
 '2122 N CLARK ST',
 '4802 N BROADWAY',
]

from fnmatch import fnmatchcase
for i in addresses:
 if fnmatchcase(i, '*ST'):
  print(i)

for l in addresses:
 if fnmatchcase(l, '54[0-9][0-9] *CLARK*'):
  print(l)

#(2.6)searching and replacing case insensitive text
"""to perform case insensitive text operations use INGNORECASE
 flag from various operations"""
import re

text = 'UPPER PYTHON, lower python, Mixed Python'
print(re.findall('python', text, flags = re.IGNORECASE))
print(re.sub('python', 'snake', text, flags= re.IGNORECASE))



#(2.5) searching and replacing text
"""for simple literal patterns  use, str.replace()"""
import re

text = 'yeah, but no, but yeah, but no, but yeah'
print(text.replace('yeah', 'yess!!!'))

"""for complicated patterns use sub() function from re module"""
from re import sub
dates = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', dates))