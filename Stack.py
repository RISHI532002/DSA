# Stack using array

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
