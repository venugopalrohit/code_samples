from basic_stack import Stack

# Problem 3.5 - Sort the content of a stack in ascending order (smallest element is at the top), with the constraint
# that you can only use one other data structure - another stack
# The solution is straight forward and can be adopted for descending order problem as well

def sort_stack(s1):

    print("Sorting stack: ")
    # Create temporary stack - s2
    s2 = Stack()

    # Push all elements into s2, while maintaining a descending order of elements
    while(s1.is_empty() == False):
        temp = s1.pop()
        while((s2.is_empty() == False) and (temp < s2.peek())):
            s1.push(s2.pop())
        s2.push(temp)

    # Push elements back into s1, resulting in ascending order of elements
    while(s2.is_empty() == False):
        s1.push(s2.pop())


def populate_stack(s, elem_list):
    for i in elem_list:
        test_stack.push(i)


# Main
elem_list = [3,5,2,8,7,2,3,33,2,1,445]
test_stack = Stack()
populate_stack(test_stack, elem_list)
sort_stack(test_stack)
print("Results:")
test_stack.print_stack()


