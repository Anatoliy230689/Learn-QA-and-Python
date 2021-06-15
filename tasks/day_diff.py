def days_diff(a, b):
    from datetime import datetime
    import datetime
    # your code here
    date1 = datetime.date(*a)
    date2 = datetime.date(*b)
    res = str(date2-date1)

    fres = ''
    for i in res:
        if i.isdigit():
            fres+=i
        elif i == '-':
            pass
        else:
            break
    r= int(fres)

    if r<0:
        return r*(-1)

    return (r)




if __name__ == '__main__':
    print("Example:")
    print(days_diff((2014, 8, 27), (2014, 8, 30)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
    # print("Coding complete? Click 'Check' to earn cool rewards!")
