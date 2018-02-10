class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(head):
    while(head != None):
        print(head.data)
        head = head.next


list1_head = Node(1)
list1_head.next = Node(2)
list1_head.next.next = Node(3)
print_list(list1_head)

list2_head = Node(10)
list2_head.next = Node(20)
list2_head.next.next = Node(30)
print_list(list2_head)