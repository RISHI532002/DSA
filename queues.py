"""
Design Queue with add/remove methods, and with capacity
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, capacity = None):
        self.front = None
        self.rear = None
        self.size = 0
        self.capacity = capacity
    
    def isEmpty(self):
        return self.front is None

    def enqueue(self, value):
        if self.capacity and self.capacity<=self.size:
            raise IndexError("Queue is full")
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
            return None
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return temp.value

    def queue_size(self):
        return self.size
    
    def get_queue(self):
        memory = []
        temp = self.front
        while temp:
            memory.append(temp.value)
            temp = temp.next
        return memory
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.front.value
