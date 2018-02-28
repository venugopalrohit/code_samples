# Google phone interview question
# Convert number into string, eg 123 -> "123"
# You can't use str(123) but you can use str(3), i.e. you can convert single digits into strings

def convert_to_string(input_number):
    number_string = ""
    # Check if input number was passed
    if(input_number == None):
        return None
    # Check if input was 0, then return string "0"
    if(input_number == 0):
        return(str(0))

    #make sure that the number is integer
    input_number = int(input_number)
    #Check if the number is negative
    is_neg = False
    if(input_number < 0):
        is_neg = True
        input_number =  abs(input_number)

    # Split the input number into digits, starting from the units place and append to a string
    # Number will be formed in the reverse order

    while(input_number > 0):
        rem = input_number % 10
        number_string += str(rem)
        input_number = int(input_number/10)

    if(is_neg):
        number_string += "-"

    return(number_string[::-1])
    #return(''.join(reversed(number_string)))

print(convert_to_string(12))