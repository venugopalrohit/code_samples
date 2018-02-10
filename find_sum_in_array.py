# This program aims to find the pair of elements that sum up to a given value
# E.g. In the list [1,2,3,4,5,2,4], find all pairs that sum up to 4
# the answer will be [(1,3), (2,2)]
# The numbers in the list can be negative or positive, non-sorted and can be repeated
# The function must a list of pairs

def find_pairs(input_array, sum):
    complement_hash = {}
    pair_list = []

    for num in input_array:
        if num in complement_hash:
            #pair found
            #Check how many pairs can be formed with multiple instances
            for i in range(0, complement_hash[num]):
                #print(num, -num)
                pair_list.append((num, sum - num))
        elif (sum - num) in complement_hash:
            complement_hash[(sum-num)] += 1
        else:
            complement_hash[(sum-num)] = 1

    return pair_list

#input_array = [1,1,-1,-1,4,5,-5]
input_array = [-3,-4,-4,-4,-10,3,3]
sum = -7
print(find_pairs(input_array, sum))