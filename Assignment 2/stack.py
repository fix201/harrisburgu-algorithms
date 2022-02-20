# implementing stacks data structure using linked list
class Node(object):
    """ A Singly-linked lists' node. """
    def __init__(self, data=None, link=None):
        self.data = data
        self.link = link

class Stack(object):
    def __init__(self):
        self.top = None
        self.count = 0
    
    def push(self, data): # add an element to the top of the stack
        temp = Node(data, self.top)
        self.top = temp

    def pop(self): # remove an element from the top of the stack
        if self.isempty():
            print("There are no elements in the stack")
            return
        temp = self.top
        self.top = self.top.link
        temp.link = None

    def peek(self): # look at the element at the top of the stack
        if self.isempty():
            print("There are no elements in the stack")
        else:
            print(self.top.data)

    def isempty(self): # check is the stack is empty
        if self.top == None:
            return True
        else:
            return False
