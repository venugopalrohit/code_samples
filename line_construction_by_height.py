# Google interview Question
# https://discuss.leetcode.com/topic/24320/line-reconstruction-by-height
# https://www.careercup.com/question?id=4699414551592960

# The solution is 2 step
# 1. Sort the tuples in ascending order of height, with the same heights being further sorted by the second element in
# the tuple, eg (5,0) and (5,2) will be sorted in the order (5,0) and (5,2) because heights (5) are the same, but the
# element is different.
# 2. Once sorted, starting from the last element in the sorted array, insert into the "result_array"
# Using the second element in the tuple as index, insert elements from the sorted array into the "result_array"
# Eg. (4,3) will go into the index 3 of the result array, (5,0) will go into index 0 (first element) of result array

class person:
    def __init__(self, name = None, ht = None, ahead = None):
        self.name = name
        self.height = ht
        self.ahead = ahead

    def get_name(self):
        return (self.name)

    def get_height(self):
        return (self.height)

    def get_ahead(self):
        return self.ahead






person_list = [person('A',7, 0), person('B', 4, 4), person("C", 7, 1), person("D", 5, 0), person("E", 6, 1), person("F", 5, 2)]
for i in person_list:
    print(i.get_name())

# Initial sort (step 1)

for i in range(0, len(person_list) -1 ):
    for j in range(i, len(person_list)):
        if(person_list[i].get_height() > person_list[j].get_height()):
            temp = person_list[i]
            person_list[i] = person_list[j]
            person_list[j] =  temp

print("Before::::")
for i in person_list:
    print(i.get_name() + " : " + str(i.get_height()) + " : " + str(i.get_ahead()))

# Now that person_list is sorted, we will create a new list "final_line" and add elements into it, one at a time

final_line = [person_list[-1]]

for i in range(len(person_list) - 2, -1, -1):
    final_line.insert(person_list[i].get_ahead(), person_list[i])

print("After::::")
for i in final_line:
    print(i.get_name() + " : " + str(i.get_height()) + " : " + str(i.get_ahead()))




