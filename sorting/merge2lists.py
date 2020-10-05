
def mergeboth(a, b):
    ia, ib, ic = 0,0,0
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
        if a[ia] <= b[ib]:
            print(str(a[ia]) + ' minor than ' + str(b[ib]))
            if len(c) > 1 and a[ia] < c[-1]:
                c.insert(-1, a[ia])
            else:
                c.append(a[ia])
            c.append(b[ib])
            print('Current C array')
            print(c)
        else:
            print(str(a[ia]) + ' major than ' + str(b[ib]))
            if len(c) > 1 and b[ib] < c[-1]:
                c.insert(-1, b[ib])
            else:
                c.append(b[ib])
            c.append(a[ia])
            print('Current C array')
            print(c)
        if ia == len(a) -1:
            if ib < len(b)-1:
                print('there are elements left from: ' + str(ib) )
                print('elements left from ' + str(ib))
                print(b[ib+1:])
                c.extend(b[ib+1:])
                print('Check lengths')
                print(length, len(c))
        else:
            if ib == len(b)-1:
                print('there are elements left from: ' + str(ia) )
                print('elements left from ' + str(ia))
                print(a[ia+1:])
                c.extend(a[ia+1:])
                print('Check lengths')
                print(length, len(c))
            else:
                ia += 1
                ib += 1
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
