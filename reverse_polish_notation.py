import re


def reverse_polish_notation(input_list):
    operand_stack = []

    for item in input_list:
        match_operands = re.match(r'\d+', item)
        if(match_operands):
            print(match_operands.group())


input_list = ["2222", "3", "4", "a", "-", "ass", "*", "5"]
reverse_polish_notation(input_list)