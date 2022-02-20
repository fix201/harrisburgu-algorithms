class Node:
    def __init__(self, data=None, next=None, prev=None) -> None:
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        
    def insert(self, data):
        temp = Node(data, None, None)
        if self.head == None:
            self.head = temp
            self.tail = self.head
        else:
            temp.prev = self.tail
            self.tail.next = temp
            self.tail = temp
        self.count += 1
    
    def traverse(self):
        current = self.head
        while current:
            print(current.data) 
            current = current.next
            pass
    
class UndoRedoApp(DoublyLinkedList):
    def __init__(self):
        super().__init__()
        self.current = self.tail

    def do(self, data, choice):
        self.current = self.tail
        if choice == 'create':
            self.append(data)
            

lst = DoublyLinkedList()
lst.insert([1,2,3,4])
lst.insert([1,2,3,4,5])
lst.traverse()
