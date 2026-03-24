class Node:
    def __init__(self, val):
        self.val = val
        self.children = []
        self.parent = None
    
    def add_node(self, child):
        child.parent = self
        self.children.append(child)
    
    def remove_children(self, child):
        self.children.remove(child)
        child.parent = None
    
    def __repr__(self):
        return f"Node f{self.val}"