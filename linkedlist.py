class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_end(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return 
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    
    def insert_at_position(self, index, value):
        if index<0:
            raise IndexError("Negative index is not allowed")
        if index==0:
            self.insert_at_beginning(value)
            return
        if not self.head:
            raise IndexError("List index out of range")
        
        temp = self.head
        for _ in range(index - 1):
            if temp.next is None:
                raise IndexError("List index out of range")
            temp = temp.next
        new_node = Node(value)
        new_node.next = temp.next
        temp.next= new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
        print("END")
