def sum_array(array):
    if len(array) == 0:
        return 0
    

    return array[0] + sum_array(array[1:])    

def count_numbers(array):
    if len(array) == 0:
        return 0
    
    return 1 + count_numbers(array[1:])
     

def find_highest_value(array):
    if len(array) == 2:
        return array[0] if array[0] > array[1] else array[1]
    sub_max = find_highest_value(array[1:])
    return array[0] if array[0] > sub_max else sub_max



print(sum_array([1, 2, 3]))
print(count_numbers([1, 2, 3]))
print(find_highest_value([1, 2, 3]))