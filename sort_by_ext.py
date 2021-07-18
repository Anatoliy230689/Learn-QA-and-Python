from typing import List

def sort_by_ext(files: List[str]) -> List[str]:
    # your code here
    l1 = []
    l11 =[]
    l2 = []
    l3 = []
    for i in files:

        if len(i.split('.')) > 2 and i.split('.')[0] !='no':
            l3.append(i)

        if (len(i.split('.')) <= 2 and i.split('.')[0] !=''):
            l2.append(i)

        if (i.split('.')[0] =='no'):
            l11.append(i)

        if (len(i.split('.')) <= 2 and i.split('.')[0] ==''):
            l1.append(i)

    def srt(l):
        return l.split('.')[1]

    l1.sort(key=srt)
    l2.sort(key=srt)
    l3.sort(key=srt)

    l1.extend(l11)
    l1.extend(l2)
    l1.extend(l3)

    for i in range(len(l1)):
        if i == len(l1)-1:
            break
        elif (l1[i].split('.')[1] == l1[i+1].split('.')[1]):
            if l1[i].split('.')[0] > l1[i+1].split('.')[0]:
                l1[i], l1[i+1] = l1[i+1], l1[i]

    return (l1)



if __name__ == '__main__':
    print("Example:")
    print(sort_by_ext(["1.aa","2.bat","1.bat","1.cad"]))

    # These "asserts" are used for self-checking and not for an auto-testing
    # assert sort_by_ext(['1.cad', '1.bat', '1.aa']) == ['1.aa', '1.bat', '1.cad']
    # assert sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']) == ['1.aa', '1.bat', '2.bat', '1.cad']
    # assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']) == ['.bat', '1.aa', '1.bat', '1.cad']
    # assert sort_by_ext(['1.cad', '1.bat', '.aa', '.bat']) == ['.aa', '.bat', '1.bat', '1.cad']
    # assert sort_by_ext(['1.cad', '1.', '1.aa']) == ['1.', '1.aa', '1.cad']
    # assert sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']) == ['1.aa', '1.bat', '1.cad', '1.aa.doc']
    # assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']) == ['1.aa', '1.bat', '1.cad', '.aa.doc']
    # print("Coding complete? Click 'Check' to earn cool rewards!")
