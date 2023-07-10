import time
print(time.time())

print(time.ctime(1671522044.2773786))

print(time.localtime())

a = time.localtime()
b = time.mktime(a)
print(b)

c = time.asctime(a)
print(c)

