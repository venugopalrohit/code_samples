from singly_linked_list import List, Node

# Problem 2.1 - Remove duplicates from unsorted list
def remove_duplicates(head_ptr):
    node_hash = {}
    p = head_ptr
    q = None
    while(p != None):
        if(p in node_hash.keys()):
            # Node found in hash table. Now move pointer over sequence of repeating elements, or until end of list
            while (p!= None and p in node_hash.keys()):
                p = p.get_next()
            # At unique element or end of list
            q.set_next(p)

        else:
            # Node not found in hash table. Add this node to the hash table and move pointers forward
            node_hash[p] = 1
            q = p
            p = p.get_next()


# Problem 2.1 - Remove duplicates from unsorted list but without using additional data structure
# This method uses two pointers, current and runner. The runner pointer starts from current and checks are following
# nodes for matches to current

def remove_duplicates_2(head_ptr):
    current = head_ptr

    while(current != None):
        runner = current

        while(runner.get_next() != None):
            if(runner.get_next().get_data() == current.get_data()):
                runner.set_next(runner.get_next().get_next())
            else:
                runner = runner.get_next()

        current = current.get_next()





# Problem 2.2 - Remove kth to last element
# k = 1: last element
# k = 2: second to last element
# k = 0 is not a valid value
def print_kth_to_last_element(head_ptr, k):
    p = head_ptr
    q = None

    while(p != None):
        p = p.get_next()
        k = k - 1
        if(k == 0):
            q = head_ptr
        if(k < 0):
            q = q.get_next()

    if(q):
        print(q.get_data())
    else:
        print("List too short!")


# Problem 2.4
# Pivot a linked list around a particular value. The list need not be sorted and the pivot need not be in the list
# The method used here is: move nodes less than pivot to the head of the list, move elements greater than or equal to
# pivot value to tail of list (using a head and tail pointer)
def pivot(head_ptr, pivot):
    head = head_ptr
    tail = head_ptr
    p = head_ptr.get_next()

    while(p != None):
        #Remember the next element
        next = p.get_next()
        if(p.get_data() < pivot ):
            p.set_next(head)
            head = p
        else:
            tail.set_next(p)
            tail = p

        p = next

    tail.set_next(None)

    return head


# Easy method to take a list of elements and insert them into linked list
def create_linked_list_from_array(linked_list, input_list):
    for elem in input_list:
        linked_list.add_node_to_list(Node(elem))


# Helper method to create a new linked list that is a reversed version of the "original list"
def reverse_linked_list(new_list, original_list):
    head = new_list
    p = original_list

    while(p != None):
        n = Node(p.get_data())
        if(head == None):
            head = n
        else:
            n.set_next(head)
            head = n

        p = p.get_next()

    return head


# Method to check whether a list is a palindrome i.e. it reads the same backwards and forward
def check_palindrome_using_reverse(original_list_head):
    reverse_list = List()
    reverse_list.head = reverse_linked_list(reverse_list.head, original_list_head)
    reverse_list.print_list()

    # Now that we have a list that is reversed, we will traverse each list until both end or a mismatch is found
    # For the lists to be palindrome, each element should match and the lists should be of equal lengths

    p = original_list_head
    q = reverse_list.head

    while((p != None) and (q != None)):
        # Data does not match, return False
        if(p.get_data() != q.get_data()):
            return False
        p = p.get_next()
        q = q.get_next()

    # We don't need to check for varying lengths because we reversed the original list. So the lengths have to be same
    # All elements matched, return true
    return True

# In this method, we use a stack to determine if the list is a palindrome. The idea is to push elements until the middle
# of the list onto a stack and then compare the remaining elements with the elements on the stack (by popping) them
# off the stack. The reversing of order (due to the stack) will imitate a two pointer method originating in the
# middle of the list and moving outwards, towards the end of the list, comparing each pair of elements as we move.
def check_palindrome_using_stack(list_head):

    # Empty list is palindrome
    if not(list_head):
        return True

    # Stack is a list
    data_stack = list()

    p = list_head
    q = list_head

    while( (p.get_next() != None) and (p.get_next().get_next() != None)):
        p = p.get_next().get_next()
        data_stack.append(q.get_data())
        q = q.get_next()

    #print("Location of P: " + str(p.get_data()))
    #print(data_stack)

    # We know that if p.next != None, then we have a list that has even number of elements
    # If the length of the list is even, q has stopped one element before the middle two elements.
    # Push the first of the middle element onto the stack
    if(p.get_next() != None):
        data_stack.append(q.get_data())

    #Moving q to location to which we can begin comparison
    q = q.get_next()

    while(q != None):
        if(q.get_data() != data_stack.pop()):
            return False
        q = q.get_next()

    return True


# Method to create intersecting lists
# Assume that the element of intersection exists in the main list
# Joining list will intersect main list at elem_to_join
def create_intersecting_lists(main_list, elem_to_join, joining_list):
    p = main_list
    # Move p to the joining element of main_list
    while(p.get_data() != elem_to_join):
        p = p.get_next()

    q = joining_list
    # Move q to the end of the joining list
    while(q.get_next() != None):
        q = q.get_next()

    # Connect the last element of joining list (q) to the elem_to_join (p) in the main list
    q.set_next(p)



# Problem 2.6
# Find the intersecting nodes between two link lists
def find_intersecting_node(list_1, list_2):
    # If either list is empty then there is no intersection point
    if(list_1 == None or list_2 == None):
        return None

    # Traverse each list and check whether they have the same end node, if they do, then the lists intersect
    # Also, determine the length of each list

    p = list_1
    list_1_len = 1
    q = list_2
    list_2_len = 1

    while(p.get_next() != None):
        p = p.get_next()
        list_1_len += 1

    while(q.get_next() != None):
        q = q.get_next()
        list_2_len += 1

    print("List 1 length: " + str(list_1_len))
    print("List 2 length: " + str(list_2_len))

    # If last elements are the same, then lists intersect otherwise return None
    if(p is q):
        print("Lists intersect")
    else:
        return None

    # Check which list is longer and advance the pointer on that list by the difference,
    # thereby chopping off the extra part

    p = list_1
    q = list_2

    if(list_1_len > list_2_len):
        # List 1 is longer, move pointer P
        len_diff = list_1_len - list_2_len
        while(len_diff > 0):
            p = p.get_next()
            len_diff -= 1
    else:
        # List 2 is longer, move pointer q
        len_diff = list_2_len - list_1_len
        while (len_diff > 0):
            q = q.get_next()
            len_diff -= 1

    print("List 1 pointer is here: " + str(p.get_data()))
    print("List 2 pointer is here: " + str(q.get_data()))

    # Move through both lists simultaneously until the intersection point is found
    while not(p is q):
        p = p.get_next()
        q = q.get_next()

    print("Intersection Node is: " + str(p.get_data()))




# Main
# Sample List
test_list = List()
elem_list = [1,1,1,1,2,3,4,1]
create_linked_list_from_array(test_list, elem_list)

test_list.print_list()


print("Solution")
# Problem 2.1
# remove_duplicates(test_list.head)
remove_duplicates_2(test_list.head)
test_list.print_list()

# Problem 2.2
#print_kth_to_last_element(test_list.head, 2)

# Problem 2.4
#test_list.head = pivot(test_list.head, 5)
#test_list.print_list()

# Problem 2.6
#print(check_palindrome_using_reverse(test_list.head))
#print(check_palindrome_using_stack(test_list.head))

# Problem 2.7
# joining_list = List()
# elem_list = [20, 30]
# create_linked_list_from_array(joining_list, elem_list)
# joining_list.print_list()
#
# create_intersecting_lists(test_list.head, 8, joining_list.head)
# test_list.print_list()
# joining_list.print_list()
#
# mock_list = List()
# elem_list = [1,2,3,4,5,6,7,8]
# create_linked_list_from_array(mock_list, elem_list)
#
#
# find_intersecting_node(test_list.head, joining_list.head)