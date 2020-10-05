

def divide(temp_list, unsorted_list):
    print('entering divide')
    if len(unsorted_list) == 1:
        temp_list.append(unsorted_list)
    else:
        divide(temp_list, unsorted_list[len(unsorted_list)//2:])
        divide(temp_list, unsorted_list[:len(unsorted_list)//2])

def merge_both(a=[], b=[]):
    index, length, c = 0, len(a) + len(b), []
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
    while len(sorted_list) < length-1:
        if list_to_sort[index] <= b[index]:
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

def merge(list_to_sort, length):
    print('entering merge')
    index, sorted_list = 0, []
    print(list_to_sort)
    for i in range(0, len(sorted_list), 2):
        print('enter for loop')
        if i+1 < len(sorted_list)-1:
            print('merging both')
            merge_both(sorted_list[i], sorted_list[i+1])
        else:
            print('we reached final elements')
            merge_both(sorted_list[i], [])
    return sorted_list




if __name__ == '__main__':
    temp_list = []
    list_to_sort = [5,4,2,7,9,1]
    divide(temp_list, list_to_sort)
    print(temp_list)
    merge(temp_list, len(list_to_sort))
