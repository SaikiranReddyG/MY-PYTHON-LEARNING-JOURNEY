#file objects

with open('guess num ''if while else''.py', 'r') as f :
    size_to_read = 10

    f_contents = f.read(size_to_read)
    print(f_contents, end='*')
    #while len(f_contents) > 0 :
        #print(f_contents,end='*')

    f_contents = f.read(size_to_read)
    print(f_contents)