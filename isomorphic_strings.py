def is_isomorphic(input_string, test_string):

    #Check if the lengths of the strings to be checked are the same
    if(len(input_string)!= len(test_string)):
        return False

    #Create a hashtable, dictionary that maps chars of input string to characters of the test string. The reason to do
    #this is to make sure that a character in input string maps to one and only one character in the test string. If
    #it maps to multiple characters, then the test string can't be isomorphic.
    #e.g. in the dictionary, if a -> g, and then a -> f, then only char_dict[a] = f will be stored in the dict. This
    #will be used in the next step when the test_string is re-created
    char_dict = {}
    for k, v in zip(input_string, test_string):
        char_dict[k] = v

    print(char_dict)

    #Recreate the test string using the hash table/dictionary created above
    final_word = ""
    for i in input_string:
        final_word =  final_word + char_dict[i]

    print(final_word)

    if(final_word == test_string):
        return True
    else:
        return False

input_string = "abcd"
test_string = "xyy"

print(is_isomorphic(input_string, test_string))