# Program to find the top "n" words in a given input text
# Aim is to limit memory usage

import re

input_file = open("complex_word_count_input.txt", "r")
#Read the whole file into memory and convert to an array of strings
file_data = input_file.read()

file_data = re.findall(r'\b[a-zA-Z]{3,15}\b', file_data)
#print(file_data)

#Create hash to hold words
words_dict = {}

#Loop for each word in the array of strings
for word in file_data:
    raw_word = word.strip(" ?.,!")
    count = words_dict.get(raw_word, 0)
    words_dict[raw_word] = count + 1

print(words_dict)


input_file.close()