class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

############### Tree Traversal using DFS #################

# 1) Pre-order  -> Current - left - right
# 2) In-order   -> left - current - right
# 3) Post-order -> left - right - current

def pre_order_dfs(node):
    if node is None:
        return
    print(node.val, end=" ")
    pre_order_dfs(node.left)
    pre_order_dfs(node.right)

def in_order_dfs(node):
    if node is None:
        return
    in_order_dfs(node.left)
    print(node.val, end=" ")
    in_order_dfs(node.right)

def post_order_dfs(node):
    if node is None:
        return
    post_order_dfs(node.left)
    post_order_dfs(node.right)
    print(node.val, end=" ")
