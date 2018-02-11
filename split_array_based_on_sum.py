# Given an array of integers greater than zero, find if it is possible to split it in two
# (without reordering the elements), such that the sum of the two resulting arrays is the same.
# Print the resulting arrays.

in_arr = [1,1,1,1,1,1]
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
    elif():
        # If sum of elements on the right side (j side) is greater, then move the i index (towards the center of list)
        i = i + 1
        i_sum = i_sum + in_arr[i]
    else:
        # Sum of both sides (sub arrays) are equal
        # Here we need to check if the indices are next to each other
        if((j - i) == 1):
            #Indices are next to each other, hence we've found a perfect split
            a = i
            break
        else:
            # Here we have a choice of incrementing i or j
            i = i + 1
            i_sum = i_sum + in_arr[i]

if(i == j):
    print("No split possible")
else:
    print("Split index is : " + str(i))

