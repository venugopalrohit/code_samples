def reverse_array(input_array, low, high):
    # Check if array is empty
    if not (input_array):
        return None

    while(low < high):
        temp = input_array[low]
        input_array[low] = input_array[high]
        input_array[high] = temp
        low = low + 1
        high = high - 1

    return input_array


input_array = [0,1,2,3,4,5,6,7,8]
print(reverse_array(input_array, 0, 8))