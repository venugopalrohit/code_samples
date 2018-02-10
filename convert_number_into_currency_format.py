us_style = [3,6,9,12,15,18]
indian_style = [3,5,7,9,11,13]


def convert_number_to_string_rep(number, style):
    if(style == "indian"):
        style_arr = indian_style
    else:
        style_arr = us_style

    num_str = str(number)
    num_len = len(num_str)
    num_str = num_str[::-1]
    ret_str = ""
    index = 0

    for i in range(0, num_len, 1):
        ret_str = ret_str + num_str[i]
        if((i != num_len - 1 ) and (i + 1 == style_arr[index])):
            ret_str = ret_str + ","
            index = index + 1

    ret_str = ret_str[::-1]
    print(ret_str)


convert_number_to_string_rep(987654321, "indian")