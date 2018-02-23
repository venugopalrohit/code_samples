# Given a list of words, create a master list that has sublists that contain anagrams

# Open file that contains list of words
in_file = open("anagram_list.txt", "r")

#Create a dictionary for the analgrams - where the key is the sorted string representing characters which form the
#anagram-ic words. The value is a list of words that are anagrams
anagram_dict = {}

for ln in in_file:
    #For each line (which represents a word), first strip any spaces. Use sorted method that returns a sorted list
    #of the component characters. Finally, use join on empty string '' to convert the character list back into a string
    sorted_str = ''.join(sorted(ln.strip()))

    #If sorted character string is present in dict, then append original word to the list of anagrams,
    #else, create a new entry in the dict, with sorted character string as key, and original word as first element
    #of anagram word list
    if(sorted_str in anagram_dict.keys()):
        anagram_dict[sorted_str].append(ln.strip())
    else:
        anagram_dict[sorted_str] = [ln.strip()]

print(anagram_dict)

in_file.close()
