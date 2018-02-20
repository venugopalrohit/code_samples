# Given an array of integers greater than zero, find if it is possible to split it in two
# (without reordering the elements), such that the sum of the two resulting arrays is the same.
# Print the resulting arrays.

# The idea here is to have to pointers (indices) at either end of the list/array and move them towards the center
# Depending on which side has the lesser sum of elements, the index at that end is moved.
# Assuming the input array is non empty
in_arr = [4,1,3,1,8,1]
# Indices into the input array
i = 0
j = len(in_arr) - 1
# Variables to maintain sum of the left side (i side) and right side (j side) of the array
i_sum = in_arr[i]
j_sum = in_arr[j]

# Try finding a split until indices reach other
while( i < j):
    if(i_sum > j_sum):
        # If sum of elements on the left side (i side) is greater, then move the j index (towards the center of list)
        j = j - 1
        j_sum = j_sum + in_arr[j]
    elif(i_sum < j_sum):
        # If sum of elements on the right side (j side) is greater, then move the i index (towards the center of list)
        i = i + 1
        i_sum = i_sum + in_arr[i]
    else:
        # Sum of both sides (sub arrays) are equal
        # Here we need to check if the indices are next to each other (which indicates a perfect split)
        if((j - i) == 1):
            #Indices are next to each other, hence we've found a perfect split
            break
        else:
            # Here we have a choice of incrementing either i or j. Doesn't matter which
            i = i + 1
            i_sum = i_sum + in_arr[i]

if(i == j):
    print("No split possible")
else:
    print("Input array can be split as: ", end="")
    print(in_arr[:i+1], end=" , ")
    print(in_arr[i+1:])

