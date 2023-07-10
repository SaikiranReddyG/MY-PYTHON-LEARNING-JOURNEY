#FILE HANDLING
F = open("abc.txt",'w')
print('file name:',F.name)
print('file mode:',F.mode)
print('is file readable:',F.readable())
print('is file writable:',F.writable())
print('is file closed:',F.closed)
F.close()
print('is file closed:',F.closed)

#writing data to text files:
d = open('abcd.txt','w')
d.write('sai\n')
d.write('kiran\n')
d.write('reddy\n')
print('the data is written')
d.close()

x = open('abcd.txt','w')
list = ['sai\n','kiran\n','reddy\n','gangula']
x.writelines(list)
print('lines written to file ')
x.close()

#to read total data from file
s = open('abcd.txt','r')
data = s.read()
print(data)

#to read 1st ten charecters
u = open('abcd.txt','r')
data = u.read(10)
print(data)


#to read data line after line
a = open('abcd.txt','r')
line1 = a.readline()
print(line1,end='')
line2 = a.readline()
print(line2,end='')
line3 = a.readline()
print(line3,end='')
a.close()

#using "with"
with open('abcd.txt','w') as g:
    g.write('gangula\n')
    g.write('sai\n')
    g.write('kiran\n')
    print('is file closed:',g.closed)
print('is file closed:',g.closed)

#tell() meathod   (to return current positin of th pointer)
z = open('abcd.txt','r')
print(z.tell())
print(z.read(2))
print(z.tell())
print(z.read(3))
print(z.tell())


#seek() meathod    (to move the cursor to specified location)
data = 'all roads lead home'
e = open('abcd.txt','w')
e.write(data)
with open('abcd.txt','r+') as e:
    text = e.read()
    print(text)
    print('the current cursor position:',e.tell())
    e.seek(17)
    print('the 2nd current cursor position:',e.tell())
    e.write('saikiranreddy!!!!')
    e.seek(0)
    text = e.read()
    print('data after modification!!!')
    print(text)


#to check if a file exists or not:
import os,sys
fname= input('enter the file name here!!')
if os.path.isfile(fname):
    print('file exists:',fname)
    f = open(fname,'r')
else:
     print('file does not exist!!',fname)
     sys.exit(0)

print('the content of the file is')
data = f.read()
print(data)


#print no of lines words charecters in the file:
import os,sys
file = input('enter the file name herer!!!')
if os.path.isfile(file):
    print('the file exists!!',file)
    f = open(file,'r')

else:
    print('the file', file, 'does not exists')
    sys.exit(0)


Lcount = Ccount = Wcount = 0
for line in f:
    Lcount = Lcount + 1
    Ccount = Ccount + len(line)
    words = line.split()
    Wcount = Wcount + len(words)

print('the total no of lines is:',Lcount)
print('the total no of charecters is:',Ccount)
print('the total no of words is:',Wcount)

#writing data to csv file
import csv
with open('emp.csv','w',newline='') as f:
    w = csv.writer(f)
    w.writerow(['ENO','ENAME','ESAL','EADDR'])
    n = int(input('enter number of employees'))

for i in range(n):
    eno = input('enter employee NO:')
    ename = input('enter the employee name')
    esal = input('enter the salery of employee:')
    eaddr = input('enter employee salery')
print('total employees data written to csv')

