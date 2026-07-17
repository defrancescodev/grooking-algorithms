def binary_search(lista, item):
    low = 0
    high = len(lista) - 1

    while low <= high:
        middle = (high + low) // 2
        guess = lista[middle]

        if guess == item:
            return middle
        if guess > item:
            high = middle - 1
        else:
            low = middle + 1
    return None


my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 1))