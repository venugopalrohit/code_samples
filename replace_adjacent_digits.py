# Google Leetcode
# https://discuss.leetcode.com/topic/55360/replace-two-adjacent-digits-with-larger-one-to-find-the-smallest-number-that-can-be-obtained

def replace_adjacent_digits(input_number):
    # Assume that min number is the one we begun with
    min_found = input_number

    digit_array = list(str(input_number))
    for i in range(0, len(digit_array)-1):
        temp_number_array = list(digit_array)
        j = i + 1;
        print("Comparing " + str(digit_array[i]) + " and " + str(digit_array[j]))
        if(digit_array[i] >= digit_array[j]):
            temp_number_array.pop(j)
        else:
            temp_number_array.pop(i)

        final_number = int("".join(temp_number_array))
        print(final_number)

        min_found = min(final_number, min_found)

    return(min_found)


input_number = 233614
print(replace_adjacent_digits(input_number))