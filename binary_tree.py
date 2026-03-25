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

def find_max_depth(root):
    """
    Find the depth using stack
    """
    if root is None:
        return 0
    stack = [(root, 1)]
    maxDepth = 0
    while stack:
        node, level = stack.pop()
        maxDepth = max(maxDepth, level)
        if node.left:
            stack.append((node.left,level+1))
        if node.right:
            stack.append((node.right,level+1))
    return maxDepth