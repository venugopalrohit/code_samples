# Program to find the top "n" words in a given input text
# Aim is to limit memory usage - though I am reading the entire file into memory :(

# The idea here is to read the file into a string, and then use a regex to weed out small words
# The regex returns a list of strings that I will iterate over and store in a hash, along with frequency
# Finally get a sorted representation of the hash, using the operator module and sorted method

import re
import operator

input_file = open("word_count_input.txt", "r")
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

# Finally, get a sorted version of the dictionary based on values
# Using the operator module which I don't fully understand
sorted_keys = sorted(words_dict.items(), key=operator.itemgetter(1), reverse=True)
print(sorted_keys)

input_file.close()