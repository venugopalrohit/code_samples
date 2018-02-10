# Check if two string are permutations of each other
# From green book, problem 1.2, page 90

def check_permutation_using_hash(str1, str2):
    # Check if the strings are of the same length. Permuatations must be of the same length
    if(len(str1) != len(str2)):
        return False

    # Hash to store the occurrances of characters in str1
    char_hash = {}

    #Add characters from str1 to hash
    for ch in str1:
        if(ch in char_hash.keys()):
            char_hash[ch] = char_hash[ch] + 1
        else:
            char_hash[ch] = 1

    print(char_hash)

    #Move through str2, and remove occurances of characters from char_hash.
    #If the strings are permutations, then the hash should be empty after str2 is processed

    for ch in str2:
        if(ch in char_hash.keys()):
            char_hash[ch] = char_hash[ch] - 1
            # Remove K,v from char_hash if frequency of character is down to 0
            if(char_hash[ch] < 1):
                char_hash.pop(ch)
        else:
            #Character was not in hash (and hence in str1), hence str2 in not a permuatation of str1
            return False

    return(not(char_hash))


def check_permutation_using_sorting(str1, str2):
    # Check if lengths of the strings are the same, else not permutation
    if(len(str1) != len(str2)):
        return False
    str1 = ''.join(sorted(str1))
    str2 = ''.join(sorted(str2))

    #If sorted strings are the same, then the strings are permutations of each other
    if(str1 == str2):
        return True
    else:
        return False

# Driver

str1 = "zab\nac\txxd\tef"
str2 = "zab\nac\txd\tef"
print(check_permutation_using_hash(str1, str2))
print(check_permutation_using_sorting(str1, str2))