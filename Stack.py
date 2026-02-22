"""
Stack using python list
"""

class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.memory = [None] * self.capacity
        self.top = -1
    
    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.capacity == self.top + 1

    def peek(self):
        if self.top == -1:
            print("Stack is empty")
            return None
        return self.memory[self.top]
    
    def push(self, value):
        if self.isFull():
            print("Stack overflow")
            return
        self.top+=1
        self.memory[self.top] = value
    
    def pop(self):
        if self.isEmpty():
            return None
        value = self.memory[self.top]
        self.memory[self.top] = None
        self.top -= 1
        return value

    def getElements(self):
        if self.isEmpty():
            return None
        return self.memory[:self.top+1]

"""
Stack using point and Nodes
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class StackLL:
    def __init__(self):
        self.top_node = None
        self.size = 0
    
    def isEmpty(self):
        return self.size == 0
    
    def push(self, value):
        new_node = Node(value=value)
        if self.top_node is None:
            self.top_node = new_node
        else:
            new_node.next = self.top_node
            self.top_node = new_node
        self.size += 1
    
    def pop(self):
        if self.isEmpty():
            return None
        temp = self.top_node
        self.top_node = self.top_node.next
        self.size -= 1
        return temp.value
    
    def get_stack(self):
        memory = []
        temp = self.top_node
        while temp:
            memory.append(temp.value)
            temp = temp.next
        return memory