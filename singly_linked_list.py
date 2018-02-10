class Node:
    def __init__(self, value, next_ptr=None):
        self.data = value
        self.next = next_ptr

    def set_data(self, value):
        self.data = value

    def get_data(self):
        return(self.data)

    def set_next(self, next_ptr):
        self.next = next_ptr

    def get_next(self):
        return(self.next)

    def __hash__(self):
        return hash(self.data)

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return (self.data == other.data)
        return False


class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def add_node_to_list(self, node_to_add):
        #This is the first node to be added to linked list
        if(self.head == None):
            self.head = node_to_add
            self.tail = node_to_add
        else:
            #Add the node to the end of list, denoted by the tail pointer
            self.tail.set_next(node_to_add)
            self.tail = node_to_add
        #Increment counter
        self.count += 1

    def print_list(self):
        p = self.head
        print("Printing List:")
        while(p != None):
            print(p.get_data())
            p = p.get_next()
        
