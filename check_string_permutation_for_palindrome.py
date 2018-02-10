# This program identifies if the permutations of a given string can result in a palindrome
# Green book, problem 1.4, page 91


# The idea behind solving this problem is to realize that palindromes are mirrored between a center point. This means
# they will have an equal number of characters on either side. This leads to the observation that the frequency of
# characters must be even (there can be at most one odd number character).
# For eg. aabbcc will give you abccba, which is a palindrome that contains, 2 occurrances of a, b and c
# abcba is also a palindrome with 1 odd character - c
# aaab is cannot result in palindrome because it has 2 odd numbered characters, a and b

def check_permutation_for_palindrome_hash_table(input_str):
    # dict to store frequency of characters
    char_hash = {}
    # variable to hold the count of odd numbered characters
    odd_char_count = 0

    for ch in input_str:
        # If character exists in key, increment its frequency
        if(ch in char_hash.keys()):
            char_hash[ch] = char_hash[ch] + 1
            # Check if incrementing this character frequency made is odd numbered
            if(char_hash[ch]%2 != 0):
                odd_char_count = odd_char_count + 1
            else:
                # increment made this character even numbered, so record that
                odd_char_count = odd_char_count - 1
        else:
            char_hash[ch] = 1
            odd_char_count = odd_char_count + 1


    print(odd_char_count)

    # If the number of characters in string are even, then for a palindrom, there should no character with odd freq
    if((len(input_str)%2 == 0) and (odd_char_count == 0)):
        return True
    # If the number of characters in string are odd, then for a palindrome, there should at most 1 character with odd freq
    elif((len(input_str)%2 != 0) and (odd_char_count == 1)):
        return True
    else:
        return False


# In this method, we use a bit map to efficiently store the occurrances of the characters. Since the bit starts out
# at 0, if at the end the bit is 0, it means that it has occurred even number of times. A '1' indicates that the bit
# has occurred odd number of times. Using the resulting bit map, we can determined if all characters have occurred
# even number of times or if more than one character has occurred odd number of times.

# For simplicity, we will consider just lower case characters

def check_permutation_using_bit_map(input_str):

    bit_map = 0

    for ch in input_str:
        mask = 1 << (ord(ch) - 97)
        if((bit_map & mask) == 0):
            bit_map |= mask
        else:
            bit_map &= ~mask

    print(bin(bit_map))

    # If the length of input string is even, then all entries in bit map must be 0 (i.e. no odd occurring characters)
    if((len(input_str)%2 == 0) and bit_map == 0):
        return True
    elif((len(input_str)%2 == 0) and bit_map != 0):
        return False
    else:
        # Here is the magic method - subtract 1 from bitmap and "and" the resulting value with bitmap
        # If the bitmap has only a single '1', then result of this operation will be a 0
        return((bit_map & (bit_map - 1)) == 0)





# Driver
input_str = "abcaaa"
print(check_permutation_for_palindrome_hash_table(input_str))
print(check_permutation_using_bit_map(input_str))