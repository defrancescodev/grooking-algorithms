def searchLowest(array):
    lowest = array[0]
    lower_index = 0
    for i in range(1, len(array)):
        if array[i] < lowest:
            lowest = array[i]
            lower_index = i
    return lower_index
    
def selectionSort(array):
    new_array = []
    for i in range(len(array)):
        lowest = searchLowest(array)
        new_array.append(array.pop(lowest))
    return new_array

print(selectionSort([5, 3, 6, 2, 10]))