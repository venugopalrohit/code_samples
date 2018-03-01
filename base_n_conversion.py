# Program to convert a given number into a base n representation or a base representation into a number

import math

#Creating two hashes that will map numbers to literals (depending on base) and literal back to number
num_to_literal = {}
for k,v in zip(range(0,10), range(0,10)):
    num_to_literal[k] = v

num_to_literal[10] = 'A'
num_to_literal[11] = 'B'
num_to_literal[12] = 'C'
num_to_literal[13] = 'D'
num_to_literal[14] = 'E'
num_to_literal[15] = 'F'

literal_to_num = dict((str(v),k) for k,v in num_to_literal.items())

print(literal_to_num)

def convert_number_into_base(number, base):
    if(number >= base):
        convert_number_into_base(number//base, base)
    print(num_to_literal[number%base], end=' ')


def convert_to_number(representation, base):
    number_of_bits = len(representation)
    num  = 0
    for ch in representation:
        #print(type(ch))
        #print(literal_to_num.get(ch))
        number_of_bits = number_of_bits - 1
        num = num + (literal_to_num.get(ch) * math.pow(base,number_of_bits))
    print(num)



# This program assumes that the caller will faciliate the adjustment for negative integers
# convert_to_number("E1", 16)
convert_number_into_base(21, 2)
convert_number_into_base(21, 8)
convert_number_into_base(21, 16)
