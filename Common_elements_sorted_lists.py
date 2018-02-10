list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_b = [2, 5, 7, 9, 10, 11, 12 ]

len_a = len(list_a)
len_b = len(list_b)
i = 0
j = 0

while((i < len_a) and (j < len_b)):
    if(list_a[i] < list_b[j]):
        i = i + 1
    elif(list_a[i] > list_b[j]):
        j = j + 1
    else:
        print(str(list_a[i]) + " " + str(list_b[j]))
        i = i + 1
        j = j + 1
