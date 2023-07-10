#decorator function
""" (it is a function which take a function as a arguement and extend
its functionality and return modified function with extended functionality)"""
def decor(func):
    def inner(name):
        if name == 'reddy':
            print('have a very bad morning!!!!')
        else:
            func(name)

    return inner
@decor
def wish(name):
    print('hello', name, "good morning!!!!")

#call same function with and without decorator
def decor(func):
    def inner(name):
        if name == 'reddy':
            print('have a very bad morning!!!!')
        else:
            func(name)

    return inner


def wishing(name):
    print('hello', name, "good morning!!!!")


decorfunction = decor(wishing)

wishing('sai')
wishing('kiran')
wishing('reddy')
decorfunction('sai')
decorfunction('kiran')
decorfunction('reddy')

def smart_division(func):
    def inner(a,b):
        print('we are dividing', a, 'with', b)
        if b == 0:
            print("OOPSS!!!....cannot divide")
            return
        else:
            return func(a,b)
    return inner

@smart_division
def divsion(a,b):
    return a/b


print(divsion(55, 33))
print(divsion(77, 0))


#decorator chaining:
def decor0(func):
    def inner(a,b):
        x = func()
        return x*x
    return inner


def decor1(func):
    def inner(a,b):
        x = func()
        return 2*x
    return inner

@decor0
@decor1
def divisioning(a,b):
    return  10

print(divisioning())