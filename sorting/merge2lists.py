
def mergeboth(a, b):
    index = 0
    length = len(a) + len(b)
    c = []
    if len(a) == 0:
        print('----- Final result -----')
        print(b)
        print('------------------------')
        return b
    if len(b) == 0:
        print('----- Final result -----')
        print(a)
        print('------------------------')
        return a
    while len(c) < length-1:
        if a[index] <= b[index]:
            print(str(a[index]) + ' minor than ' + str(b[index]))
            if len(c) > 1 and a[index] < c[-1]:
                c.insert(-1, a[index])
            else:
                c.append(a[index])
            c.append(b[index])
            print('Current C array')
            print(c)
        else:
            print(str(a[index]) + ' major than ' + str(b[index]))
            if len(c) > 1 and b[index] < c[-1]:
                c.insert(-1, b[index])
            else:
                c.append(b[index])
            c.append(a[index])
            print('Current C array')
            print(c)
        if index == len(a) -1:
            if index < len(b)-1:
                print('there are elements left from: ' + str(index) )
                print('elements left from ' + str(index))
                print(b[index+1:])
                c.extend(b[index+1:])
                print('Check lengths')
                print(length, len(c))
        else:
            if index == len(b)-1:
                print('there are elements left from: ' + str(index) )
                print('elements left from ' + str(index))
                print(a[index+1:])
                c.extend(a[index+1:])
                print('Check lengths')
                print(length, len(c))
            else:
                index += 1
    print('----- Final result -----')
    print(c)
    print('------------------------')
    return c

def test1():
    print('starting test1')
    a = [1,2,5,8,8]
    b = [3,6,7,7]
    assert mergeboth(a, b) == [1, 2, 3, 5, 6, 7, 7, 8, 8]
    print('------------------------')


def test2():
    print('starting test2')
    f = [1,4,6,8,9]
    g = [2,5,7]
    assert mergeboth(f,g) == [1, 2, 4, 5, 6, 7, 8, 9]
    print('------------------------')


def test3():
    print('starting test3')
    d = [2,6,8]
    e = [1,7,9]
    assert mergeboth(d,e) == [1, 2, 6, 7, 8, 9]
    print('------------------------')

def test4():
    print('starting test4')
    a = [1,3,5,7]
    b = [2,4,6]
    assert mergeboth(a,b) == [1, 2, 3, 4, 5, 6, 7]
    print('------------------------')

def test5():
    print('starting test5')
    a = [1,2,9]
    b = [5,7,8]
    assert mergeboth(a,b) == [1, 2, 5, 7, 8, 9]
    print('------------------------')

def test6():
    print('starting test6')
    a = [1,2]
    b = []
    assert mergeboth(a,b) == [1, 2]
    print('------------------------')

def test7():
    print('starting test7')
    a = []
    b = []
    assert mergeboth(a,b) == []
    print('------------------------')

def test8():
    print('starting test8')
    a = []
    b = [1,2]
    assert mergeboth(a,b) == [1, 2]
    print('------------------------')

if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()
