
from datetime import datetime
from time import sleep


def dec(func):
    def wrapper():
        start = datetime.now()
        func()
        print((datetime.now()) - start)
    return wrapper
@dec
def func():
    sleep(1)
func()

# Передаем аргументы

def dec1(arg):
    print (arg)
    def outor(func1):
        def wrapper(*args, **kwargs):
            start = datetime.now()
            func1(*args, **kwargs)
            print((datetime.now()) - start)
        return wrapper
    return outor

@dec1('name')
def func1(n):
    l = [x for x in range(n) if x%2 == 0]
    print(l)

l1 = func1
a = l1(10)

