#SET{}        (group of unique values as a single entitiy)
# (duplication not allowed)
#(indexing and slicing not alllowed)
# (set objects are mutable)

lit = [23,53,7,6,12]
lit1 = set(lit)
print(lit1)
print(type(lit1))

se = set(range (8))
print(se)

s = {}
print(type(s))
s1 = set()
print(type(s1))


#different functions of a set

#add()
st = {23,53,7,6,12}
st.add(99)
print(st)

#update()
so = {23,53,7,6,1,45,67}
sp = {34,356,67,2,234,34}
so.update(sp,range(7))
print(so)

#copy()
sq = {23,53,7,6,1,45,67}
sw = sq.copy()
print(sw)

#pop()
su = {23,53,7,6,1,45,63,45}
print(su)
print(su.pop())
print(su)

#remove()
sp = {23,53,7,6,1,45,63,45}
print(sp)
sp.remove(63)
print(sp)
sp.remove(533)
print(sp)

#discard()
sl = {23,53,7,6,1,45,63,45}
print(sl)
sl.discard(63)
print(sl)
sl.discard(533)
print(sl)

#clear()
sk = {23,53,7,6,1,45,63,45}
print(sk)
sk.clear()
print(sk)

#mathematical operations

#union()
x = {10, 20, 30, 40}
y = {30, 40, 50, 60}
print(x.union(y))
print(x|y)
#intersection()
print(x.intersection(y))
print(x&y)
#difference()
print(x.difference(y))
print(x-y)
#symmetric difference()
print(x.symmetric_difference(y))
print(x^y)

#MEMBERSHIP

a = set('saireddy')
print(a)
print("a" in a)
print('z' in a)

#program to identify vowels present in sentence
x = set(input('enter a required sentence:'))
v = {'a','e','i','o','u'}
d = x.intersection(v)
print('the vowels present in',x,'are',d)