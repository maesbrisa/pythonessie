def giveMeOccurrences(string):
    dict_results = {}
    for char in string:
        if char in dict_results:
            dict_results[char] += 1
        else:
            dict_results.update({char:1})
    return dict_results

if __name__ == '__main__':
    string = 'archlinux.org'
    print(giveMeOccurrences(string))

