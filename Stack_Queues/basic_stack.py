# Implementation of a basis stack in python
# You can always get around the maintaining the top variable but its a minor overhead, rather than computing the length
# of the array each time

class Stack:

    def __init__(self):
        self.data_list = []
        self.top = -1

    def push(self, num):
        self.data_list.append(num)
        self.top += 1

    def pop(self):
        if(self.top == -1):
            return None
        else:
            self.top -= 1
            return(self.data_list.pop())

    def peek(self):
        if (self.top == -1):
            return None
        else:
            return (self.data_list[-1])

    def print_stack(self):
        print("Printing Stack (Bottom UP): ")
        for i in self.data_list:
            print(i)

    def is_empty(self):
        return(self.top == -1)
