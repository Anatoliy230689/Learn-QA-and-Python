from functools import reduce
# Факториал 1
f = int(input('число: '))
count = 1
for i in range(1,f+1):
    count *= i
print(count)
# Факториал 12
x = reduce(lambda x,y: x*y, range(1, f+1))
print(x)
# числа фибоначи
l = [0,1]
for i in range(100):
    r = l[i] + l[i+1]
    l.append(r)
print(l)





