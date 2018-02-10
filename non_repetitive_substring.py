input_str = 'abcbaedm'
input_len = len(input_str)

max_len = 0
max_str = ''

current_sub = ''
current_sub += input_str[0]
current_len = 1
i = 1

#for i in range(1, (input_len) ):
while i < input_len:
    # check if the current character in the input string is present in our current substring
    if(current_sub.find(input_str[i]) != -1):
        # check if the current substring we've found is greater than the max we've had before
        if(current_len >= max_len):
            max_str = current_sub
            max_len = current_len

        #Backtrack to see which character in the substring matched, so that we can advance 'i' to that position
        #directly
        match_char = input_str[i]
        j = i - 1
        while(input_str[j] != match_char):
            j = j - 1
        # move i to one position beyond the matched character so we can begin a new substring
        i = j + 1
        # Beginning the next substring, after the previously matched character
        current_sub = input_str[i]
        current_len = 1
    else:
        # Append the next character to current_substring
        current_sub += input_str[i]
        current_len = current_len + 1

    i = i + 1

if(current_len >= max_len):
    max_str = current_sub
    max_len = current_len


print(max_str)




