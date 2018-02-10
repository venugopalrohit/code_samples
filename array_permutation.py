#http://www.programcreek.com/2013/02/leetcode-permutations-java/
#http://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/

def generate_permutation(input_arr, start, end):

    if(end > len(input_arr) - 1):
        print(input_arr)
        return

    while(end < len(input_arr)):
        input_arr[start], input_arr[end] = input_arr[end], input_arr[start]
        #print(input_arr)
        generate_permutation(input_arr, start + 1, start + 1)
        input_arr[end], input_arr[start] = input_arr[start], input_arr[end]
        end = end + 1

input_array = [1,2,3]
generate_permutation(input_array, 0, 0)

