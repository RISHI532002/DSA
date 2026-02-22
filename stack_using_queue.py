"""
This is implementation of stack data structure using a queue 
(Here i am implementating the queue using linked list)
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class MyQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    
    def isEmpty(self):
        return self.front is None

    def enqueue(self, value):
        new_node = Node(value)
        if self.isEmpty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1
    
    def dequeue(self):
        if self.isEmpty():
            raise IndexError("List is empty")
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return temp.value
    
    def get_size(self):
        return self.size

    def peek(self):
        return self.front.value

class MyStack():
    
    def __init__(self):
        self.q = MyQueue()
    
    def push(self, x):
        self.q.enqueue(value=x)
        # reverse the existing elements
        for _ in range(self.q.get_size() - 1):
            self.q.enqueue(self.q.dequeue)
        
    def pop(self):
        return self.q.dequeue()

    def top(self):
        return self.q.peek()

    def empty(self):
        self.q.isEmpty()