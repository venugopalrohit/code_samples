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

input_array = [1,2,3,4,5,6,7]
rotation_side = "right"
rotation_count = 3

# If rotation count is greater than the length of the array, then we need to only rotate it by the mod of the length of
# the array. For eg, left or right rotation by 5 of [1,2,3,4,5] will result in the same array i.e. [1,2,3,4,5]. So if
# rotation is greater than the length, just do a mod, e.g. rotation count = 8  then 8%5 = 3, real rotation count.

if(rotation_side == "left"):
    #Left rotation means we need to reverse the parts (defined by the sides) and reverse the whole array
    reverse_array(input_array, 0, rotation_count - 1)
    reverse_array(input_array, rotation_count, len(input_array) - 1)
    reverse_array(input_array, 0, len(input_array) - 1)
    print(input_array)
else:
    # Right rotation means we need to reverse the whole array and reverse the parts (defined by the sides)
    reverse_array(input_array, 0, len(input_array) - 1)
    reverse_array(input_array, 0, rotation_count - 1)
    reverse_array(input_array, rotation_count, len(input_array) - 1)
    print(input_array)