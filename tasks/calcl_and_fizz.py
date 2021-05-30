# fizz buzz

for i in range(100):
    if i%3 == 0 and i!=0:
        print('fizz')
    elif i%5 == 0 and i!=0:
        print('buzz')
    else:
        print(i)

exit()
#calck
calck = {
    '+':lambda x, y:x+y,
    "-":lambda x,y:x-y,
    '*':lambda x,y:x*y,
    "/":lambda x,y:x/y
}

assert calck['+'](1,3) == 4
assert calck['-'](2,3) == -1
assert calck['*'](4,5) == 20
assert calck['/'](64,8) ==8
