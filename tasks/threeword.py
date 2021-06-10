def checkio(words: str) -> bool:

    l = words.split()
    print(l)
    if len(l)<3:
        return False
    for i in range(len(l)):
         if l[i].isalpha() and l[i+1].isalpha() and l[i+2].isalpha():
             res = True
             break
         elif int(i) == int((len(l)-2)):
             break
         else:
            res = False
    return res

print(checkio('one two 3 four five six 7 eight 9 ten eleven 12'))if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))

    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"

if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))

    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"