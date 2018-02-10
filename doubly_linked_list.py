class Node:
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

    def get_data(self):
        return (self.data)

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return (self.next_node)

    def set_prev_node(self, prev_node):
        self.prev_node = prev_node

    def get_prev_node(self):
        return (self.prev_node)

class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def insert_node(self, data):
        if(self.head == None):
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.set_next_node(Node(data, None, self.tail))
            self.tail = self.tail.get_next_node()

        self.count += 1

    def print_list(self):
        p = self.head
        while(p != None):
            print(p.get_data())
            p = p.get_next_node()

    def print_list_reverse(self):
        p = self.tail
        while (p != None):
            print(p.get_data())
            p = p.get_prev_node()

    def get_count(self):
        return (self.count)

    def list_search(self, req_data):
        p = self.head
        while(p != None):
            if(p.get_data() == req_data):
                return True
            p = p.get_next_node()
        return False

#To Do
#Add method for insert node before or after
#Add method to delete node





mylist = List()
#
for i in range(0, 10):
    mylist.insert_node(i)
#
mylist.print_list_reverse()
print(mylist.list_search(56))
# print(mylist.delete_node(23))
# mylist.print()