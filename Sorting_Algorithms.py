def bubble_sort(input_array):
    for i in range(len(input_array) - 1):
        for j in range(i, len(input_array)):
            if(input_array[i] > input_array[j]):
                input_array[i], input_array[j] = input_array[j], input_array[i]
        #print(input_array)

    #print("Answer:: ")
    return input_array

def selection_sort(input_array):
    for i in range(len(input_array) - 1):
        min = input_array[i]
        index_of_least = i
        for j in range(i, len(input_array)):
            if(input_array[j] < min):
                index_of_least = j
                min = input_array[j]

        input_array[i], input_array[index_of_least] = input_array[index_of_least], input_array[i]
        print(input_array)

    print("---------------------")
    return input_array


def insertion_sort(input_array):
    for i in range(1, len(input_array)):
        temp = input_array[i]
        j=i
        while(j > 0 and input_array[j-1] > temp):
            input_array[j] = input_array[j-1]
            j = j - 1

        input_array[j] = temp
        print(input_array)

    print("---------------------")
    return input_array

input_array = [8,5,3,1,9,6,0,7,4,2,5]
#input_array = [5,3,1,6,2,5]

#print(bubble_sort(input_array))
#print(selection_sort(input_array))
print(insertion_sort(input_array))