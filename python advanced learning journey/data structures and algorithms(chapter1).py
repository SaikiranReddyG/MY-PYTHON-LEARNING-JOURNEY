#(1.1)unpacking a sequence into saperate variables
p = 4, 5
x, y = p
print(x)
print(y)

data = ['sai', 55,55.7, (2012, 12, 21)]
name, share, price, date = data
print(name)
print(share)
print(price)
print(date)
"""unpacking not only works with tuples or lists, but also with
strings, files, iterators, and generators"""
s = 'hello'
a, b, c, d, e = s
print(a)
print(b)

"""sometimes you may want to discard some items
...there is no special sintax for this 
but you can pick a throwaway variablee for this"""
data = ['sai', 55,55.7, (2012, 12, 21)]
_, shares, _, price = data
print(shares)
print(price)

#(1.2)unpacking elements from iterables
"""sometimes you need to unpack N no of elements,
 but the iterable may be longer than the N values """

"""we can solve this by 'star expression'   """

#def drop_first_last(grades):
    #first, *middle, last = grades
    #return average(middle)
record = ('saikiran', 'reddy@gmail.com', '7659996553', '7661880608')
name, gmail, *ph_numbers = record
print(name)
print(gmail)
print(ph_numbers)


records = [('foo', 1, 2),
           ('bar', 'hello'),
           ('foo', 3, 4)]

def d_f(x, y):
    print('foo', x, y)

def d_b(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        d_f(*args)
    elif tag == 'bar':
        d_b(*args)


"""sometimes you might want to unpack values and thrrow them away"""
record = ('sai', 55,55.7, (2012, 12, 21))
name, *_, (*_, year) = record
print(name)
print(year)

"""if you have a list you can easily 
split it into head and tail combination"""

items = [1, 2, 3, 4, 5, 6, 7, 8,]
head, *tail = items
print(head)
print(tail)


#(1.3)keeping the last N items

"""collections.deque = it is a subclass of list and 
provides fast and efficient appending/ popping from both ends """

"""feauters of deque are= 
time complexity for adding and removing elements  from both ends
can have max size or extended indefinetly
provide thread safe memory efficient implementation"""

from collections import deque
q = deque(maxlen=5)
q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)
q.append(6)
q.append(7)
print(q)

"""deque is used whenever you need a simple queue structure"""
"""if you dont give a max len, you will get a unbounded list"""
from collections import deque
w = deque()
w.append(1)
w.append(2)
w.append(3)
w.append(4)
print(w)
w.appendleft(7)
print(w)
w.pop()
print(w)
w.popleft()
print(w)

#finding the largest or smallest of N numbers

"""heapq module = provides the implementation of the heapq algorithm(priority based algorithm)
it is a specilized tree based data structure that is commonly used in algorithms for sorting, searching, and graph transversal"""


import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))
print(heapq.nlargest(11, nums))
print(heapq.nsmallest(11, nums))

import heapq
import time
portfolio = [
 {'name': 'IBM', 'shares': 100, 'price': 91.1},
 {'name': 'AAPL', 'shares': 50, 'price': 543.22},
 {'name': 'FB', 'shares': 200, 'price': 21.09},
 {'name': 'HPQ', 'shares': 35, 'price': 31.75},
 {'name': 'YHOO', 'shares': 45, 'price': 16.35},
 {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
cheap = heapq.nsmallest(4, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(4, portfolio, key=lambda s: s['price'])
badshare = heapq.nsmallest(5, portfolio, key=lambda c: c['shares'])
goodshare = heapq.nlargest(5, portfolio, key=lambda c: c['shares'])

print(cheap)
time.sleep(2)
print(expensive)
time.sleep(2)
print(badshare)
time.sleep(2)
print(goodshare)

#(1.6)mapping keys to multiple values in a dictionary
"""if you want to store multiple values to a key, you can store multiple values  in an another list/set"""
n = {'a':[1,2,3],
     'b':[4,5,6]}

x = {'c':[7,8,9],
    'd':[10,11,12]}

print(n)
print(type(n))
print(x)
print(type(x))

"""to easily construct such dicts, we can use defaultdict form collections"""
from collections import defaultdict
b = defaultdict(list)
b['e'].append(1)
b['f'].append(2)
b['e'].append(3)
b['f'].append(4)
b['e'].append(5)
b['f'].append(6)
b['e'].append(7)
b['f'].append(8)
print(b)


from collections import defaultdict
l = defaultdict(set)
l['e'].add(1)
l['f'].add(2)
l['e'].add(3)
l['f'].add(4)
l['e'].add(5)
l['f'].add(6)
l['e'].add(7)
l['f'].add(8)
print(l)

#keeping dictioneries in order
from collections import OrderedDict
v = OrderedDict()
v['sai'] = 19
v['kiran'] = 56
v['reddy'] = 1956
print(v)

#calculating with dictonaries
"""in order to perform useful calculations on the dict contents,
 it is often useful to invert the keys and values  using zip()function"""
prices = {
 'ACME': 45.23,
 'AAPL': 612.78,
 'IBM': 205.55,
 'HPQ': 37.20,
 'FB': 10.75
}

min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
print(max_price)
print(min_price)

"""similarly to rank the data use zip() along with sorted()"""
price_sorted = sorted(zip(prices.values(), prices.keys()))
print(price_sorted)

#commanalities in two dicts
"""to find commanalities between dicts, just perform common set operations"""
a = {
 'x' : 1,
 'y' : 2,
 'z' : 3
}
b = {
 'w' : 10,
 'x' : 11,
 'y' : 2
}
print(a.keys() & b.keys())
print(a.items() & b.items())
print(a.keys() - b.keys())

#removing duplicates from a sequence while maintaining the order
a = [1, 5, 2, 1, 9, 1, 5, 10]
print(set(a))

#determining most frequently occuring items in a sequeence
words = [
 'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
 'my', 'eyes', "you're", 'under'
]
morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']

from collections import Counter
word_counts = Counter(words)
print(word_counts)
top_three = word_counts.most_common(4)
print(top_three)
print(word_counts['eyes'])
word_counts.update(morewords)
print(word_counts)
q = Counter(words)
p = Counter(morewords)
x = q + p
print('the total count is:', x)


#sorting a list of dictionaries by a common key

from operator import  itemgetter
rows = [
 {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
 {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
 {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
 {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print(rows_by_fname)
print(rows_by_uid)


#grouping records togather based on a feild
"""the groupby() function works by scanning a sequence and finding sequentioal runs of identical values
On each iteration it returns a value alonge with the iterator that produce all of the items in a group"""
from operator import itemgetter
from itertools import groupby
rows = [
 {'address': '5412 N CLARK', 'date': '07/01/2012'},
 {'address': '5148 N CLARK', 'date': '07/04/2012'},
 {'address': '5800 E 58TH', 'date': '07/02/2012'},
 {'address': '2122 N CLARK', 'date': '07/03/2012'},
 {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
 {'address': '1060 W ADDISON', 'date': '07/02/2012'},
 {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
 {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

rows.sort(key=itemgetter('date'))

for rows, items in groupby(rows, key=itemgetter('date')):
    print('date')
    for i in items:
        print('', i)



#filtering the sequence of elementsaddresses = [
from itertools import compress
addresses = [
 '5412 N CLARK',
 '5148 N CLARK',
 '5800 E 58TH',
 '2122 N CLARK'
 '5645 N RAVENSWOOD',
 '1060 W ADDISON',
 '4801 N BROADWAY',
 '1039 W GRANVILLE',
]
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]
more_5 = [n > 5 for n in counts]
print(more_5)

print(list(compress(addresses, more_5)))

#extracting subsets of a dictionary
from collections import namedtuple
subscriber = namedtuple('subscriber', ['addr', 'joined'])
sub = subscriber('saikiran@gmai;l.com', '2002-22-03')
print(sub)

#(1.19)transforming and reducing data at the same time
nus = [1, 2, 3, 4, 5, 6]
s = sum(x * x for x in nus)
print(s)

import os
files = os.listdir('dirname')
if any(name.endswith('.py')for name in files):
    print('there is python!!!')

else:
    print('sorry no python!!!')



#combining multiple mappings into a single mapping
"""chainmap takes multiple mappings
and makes them logically appera as one"""
from collections import ChainMap
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
c = ChainMap(a,b)
print(c['x'])
print(c['y'])
print(c['z'])
print(len(c))
print(list(c.keys()))
print(list(c.values()))
values = ChainMap()
values['x'] = 1
values = values.new_child()    #add a new mapping
values['x'] = 2
values = values.new_child()    #add a new mapping
values['x'] = 3
print(values)

values = values.parents          #discard last mapping
print(values['x'])

values = values.parents         #discard last mapping
print(values['x'])
print(values)


