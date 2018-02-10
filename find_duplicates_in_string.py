#Algorithm to check if string has all unique characters, using various methods
#From the green book, solution on page 192


def find_dup_using_list(input_str):
    # Assuming ASCII set. There can only be 128 unique characters. If greater, then at least one has been repeated
    if(len(input_str) > 128):
        return False
    # Create a list of 128 elements, all initiatized to False
    char_list = [False] * 128
    for ch in input_str:
        if(char_list[ord(ch)] == True):
            return False
        char_list[ord(ch)] = True

    return True


# For this method, we assume that we only have lower case alphabets (a to z), so an INT will work as a bit map
# However, it seems that in python, INTS really dont have a fixed size, so we can also have the whole ASCII or UNICODE set
def find_dup_using_bit_map(input_str):
    # Allowed character set is 26 long, so string greater than 26 should have duplicates
    if(len(input_str) > 26):
        return False
    # The size of this variable doesn't matter because python will resize it dynamically
    char_bit_map = 0
    for ch in input_str:
        # 96 because the first character 'a' is 97th in ASCII table, so bit for 'a' will be 1
        if(char_bit_map & (1 << (ord(ch) - 96))):
            return False
        else:
            char_bit_map = char_bit_map | (1 << (ord(ch) - 96))

    return True


# Use a hash table to find a duplicates (if key exists in hash table, then duplicate)
def find_dup_using_hash(input_str):
    # Assuming ASCII set. There can only be 128 unique characters. If greater, then at least one has been repeated
    if (len(input_str) > 128):
        return False
    # Creating empty hash to hold the unique characters
    char_hash = {}
    for ch in input_str:
        if(ch in char_hash):
            return False
        else:
            char_hash[ch] = 0

    return True



# Driver

input_str = "a"
print(find_dup_using_list(input_str))
print(find_dup_using_bit_map(input_str))
print(find_dup_using_hash(input_str))