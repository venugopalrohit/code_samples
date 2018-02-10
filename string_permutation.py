
def check_permutation(input_str, str_to_check):

    char_dict = {}

    for letter in input_str:
        if letter in char_dict:
            char_dict[letter] =  char_dict[letter] +  1
        else:
            char_dict[letter] = 1

    print(char_dict)

    for letter in str_to_check:
        if ((letter in char_dict) and (char_dict[letter] > 0)):
            char_dict[letter] = char_dict[letter] - 1
            # Removing character entries that have count as 0
            if(char_dict[letter] == 0):
                del char_dict[letter]
        else:
            return False

    # There are still elements in the char_dict meaning that all characters weren't accounted for in the permutation
    if(char_dict):
        return False
    return True

# Main function
input_str = "xyza"
str_to_check = "xyz"
print(check_permutation(input_str, str_to_check))