from collections import Counter
import string
import unittest



def count_ocurrences(array):
    occurrences = Counter()
    for element in array:
        occurrences.update(element)
    return occurrences

def can_transform(a, b):
    if len(a) != len(b):
        return False
    occ_a = count_ocurrences(a)
    occ_b = count_ocurrences(b)
    if len(occ_a) != len(occ_b):
            return False
    return True

def transform(first_string, second_string):
    first_array, second_array = list(first_string), list(second_string)
    if can_transform(first_array, second_array):
        hashmap = {}
        temp_letters = set(string.ascii_lowercase) - set(second_string)
        for index, element in enumerate(first_array):
            print('Element ' , element)
            if first_array[index] == second_array[index]:
                pass
            elif element in second_array:
                temp = temp_letters.pop()
                hashmap.update({element: temp})
                hashmap.update({temp: second_array[index]})
                second_array[index]=temp
            else:
                hashmap.update({element: second_array[index]})
            print(hashmap)
        return len(hashmap)
    else:
        return 0


class Test(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(transform('ab','ba'), 3)
    def test_basic_duplicates(self):
        self.assertEqual(transform('abb','baa'), 3)
    def test_error(self):
        self.assertEqual(transform('abb', 'adc'),0)
    def test_error_maps(self):
        self.assertEqual(transform('abb', 'abc'),0)

if __name__ == '__main__':
    unittest.main()