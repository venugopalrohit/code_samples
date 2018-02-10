#Leet code problem
# https://leetcode.com/problems/two-sum/#/description
#

def two_sum(input_array, target):
    comp_hash = {}

    for i in range(0, len(input_array)):
        if(input_array[i] in comp_hash):
            # pair found
            return(comp_hash[input_array[i]], i)
        else:
            comp_hash[target - input_array[i]] = i

    return None


input_array = [2,2,5,7]
target = 9
print(two_sum(input_array, target))
