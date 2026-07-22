def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        x = array[0]
        lowers = [i for i in array[1:] if i<= x]
        biggers = [i for i in array[1:] if i > x]
        return quick_sort(lowers) + [x] + quick_sort(biggers)

print(quick_sort([10, 5, 2, 3]))

