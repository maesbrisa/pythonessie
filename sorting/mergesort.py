

def merge_sort(original_list):
    print('entering divide')
    if len(original_list) > 1:
        middle_index = len(original_list)//2
        left = original_list[:middle_index]
        right = original_list[middle_index:]
        merge_sort(left)
        merge_sort(right)
        print('i am back!')
        left_index, right_index, original_index = 0, 0, 0
        while left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                original_list[original_index] = left[left_index]
                left_index += 1
            else:
                original_list[original_index] = right[right_index]
                right_index += 1
            original_index += 1
            print('we have just put two values in order from both halves')
            print(right[right_index-1], left[left_index-1])

        while left_index < len(left):
            print('this means that right half is out of stock')
            print(right, right_index, left, left_index)
            original_list[original_index] = left[left_index]
            left_index += 1
            original_index += 1

        while right_index < len(right):
            print('this means that left half is out of stock')
            print(right, right_index, left, left_index)
            original_list[original_index] = right[right_index]
            right_index += 1
            original_index += 1

if __name__ == '__main__':
    list_to_sort = [5,4,2,7,9,1]
    merge_sort(list_to_sort)
    print('now sorted')
    print(list_to_sort)
