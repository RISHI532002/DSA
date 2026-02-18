class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_start(self, value):
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
    
    def insert_at_index(self, index, value):
        """
        zero based index
        """
        if index < 0:
            raise IndexError("Index out of range")
        if index==0:
            self.insert_at_start(value)
            return
        if not self.head:
            raise IndexError("List is empty")
        new_node = Node(value)
        temp = self.head
        for _ in range(index-1):
            if not temp.next:
                raise IndexError("List index out of range")
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
    
    def search_by_value(self, value):
        if not self.head:
            print("List is empty")
            return False
        temp = self.head
        while temp:
            if temp.value==value:
                return True
            temp = temp.next
        return False
    
    def search_by_index(self, index):
        if not self.head:
            print("List is empty")
            return None
        if index<0:
            raise IndexError("List index out of range")
        if index==0:
            return self.head.value
        temp = self.head
        for _ in range(index-1):
            if not temp.next:
                raise IndexError("List index out of range")
            temp = temp.next
        if not temp.next:
            raise IndexError("List index out of range")
        return temp.next.value

    def display(self):
        if not self.head:
            print("None")
            return
        temp = self.head
        while temp:
            print(temp.value, end="->")
            temp = temp.next
        print("END")
