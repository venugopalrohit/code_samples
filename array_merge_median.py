array_a = [1,2,5,6,9,10]
array_b = [3,4,7,8]
array_c = []
final_array_len = 0

i = 0
j = 0

while(len(array_a) and len(array_b)):
    if(array_a[0] < array_b[0]):
        array_c.append(array_a.pop(0))
        final_array_len = final_array_len + 1

    else:
        array_c.append(array_b.pop(0))
        final_array_len = final_array_len + 1


if(len(array_a)):
    final_array_len = final_array_len + len(array_a)
    array_c.extend(list(array_a))
else:
    final_array_len = final_array_len + len(array_b)
    array_c.extend(list(array_b))

print (array_c)
print (final_array_len)

# If the number of elements in the array is odd, then the median is the middle element
if(final_array_len%2 != 0):
    median = array_c[int(final_array_len/2)]
else:
    median = (array_c[int(final_array_len/2)] + array_c[int((final_array_len/2)) +1])/2

print(median)