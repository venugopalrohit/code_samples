def remove_duplicates(input_str):

    char_dict = {}
    output_string = ""

    for letter in input_str:
        if not(letter in char_dict):
            char_dict[letter] = 1
            output_string = output_string + letter

    return output_string


# Main function
input_str = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaabbbbbbbbbbbbbbbbaaaaaaaaawwwwwwwwwwwwfffffffff"
print("Input string: " + input_str );
print("Output string: " + remove_duplicates(input_str))