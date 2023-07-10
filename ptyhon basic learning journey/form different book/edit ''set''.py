a = {1,2,3,4,5,6,'aa','dd','r'}
b = set([1,4,7,'df','ht'])
c = set()
print(len(a))
print(len(b))
for x in a:
    print(x)
c.add(4)
print(c)
c.update([4,5,"j","yy"])
print(c)
a.remove(2)
b.discard(1)
a.pop()
print(a&b)
print(a.intersection(b,c))

print(a)
print(b)
print(c)

