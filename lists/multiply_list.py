def multiply(lista):
    result = lista[0]
    for el in lista:
        result *= el
    return result

if __name__ == '__main__':
    lista = [1,2,3,4]
    print(multiply(lista))
