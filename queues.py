"""
Implement queue using Linked List
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    
    def isEmpty(self):
        return self.front is None

    def enqueue(self, value):
        new_node = Node(value)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1
    
    def dequeue(self) -> any:   
        if self.isEmpty():
            raise IndexError("Queue is Empty")
        temp_node = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return temp_node.value
    
    def queue_size(self):
        return self.size
    
    def get_queue(self):
        if self.isEmpty():
            return []
        memory = []
        temp = self.front
        while temp:
            memory.append(temp.value)
            temp = temp.next
        return memory