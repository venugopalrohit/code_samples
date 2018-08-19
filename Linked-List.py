class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data;
        self.next_node = next_node;

    def __str__(self):
        return (str(self.data))

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.count = 0

    def insert_node(self, data):
        node_to_add = Node(data)
        node_to_add.set_next(self.head)
        self.head = node_to_add
        self.count = self.count + 1

    def print(self):
        p = self.head
        while (p != None):
            print(p, end=" ")
            p = p.get_next()
        print()

    def print_count(self):
        return (self.count)

    def search(self, data):
        p = self.head
        ret_val = False;
        while (p != None):
            if (p.get_data() == data):
                ret_val = True
                break
            p = p.get_next()

        return ret_val

    def delete_node(self, data):
        if (self.head.get_data() == data):
            self.head = self.head.get_next();
            return True

        p = self.head.get_next()
        q = self.head

        while (p != None):

            if (p.get_data() == data):
                q.set_next(p.get_next())
                return True

            q = p
            p = p.get_next()

        return False

    def return_elements(self):
        p = self.head
        element_array = []
        while (p != None):
            element_array.append(p.get_data())
            p = p.get_next()

        return element_array


# mylist = LinkedList()
#
# for i in range(0, 20):
#     mylist.insert_node(i)
#
# mylist.print()
# print(mylist.delete_node(23))
# mylist.print()

number_1 = LinkedList()
number_2 = LinkedList()

number_1.insert_node(3)
number_1.insert_node(4)
number_1.insert_node(2)

number_2.insert_node(4)
number_2.insert_node(6)
number_2.insert_node(5)

number_1.print()
number_2.print()

number_1_array = number_1.return_elements()
print(number_1_array)

number_1_string = ''
for i in number_1_array:
    number_1_string += str(i)

print(number_1_string)

number_2_array = number_2.return_elements()
print(number_2_array)

number_2_string = ''
for i in number_2_array:
    number_2_string += str(i)

print(number_2_string)

print((int(number_1_string)+ int(number_2_string)))