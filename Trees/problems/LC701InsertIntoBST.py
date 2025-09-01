'''
Rule - 
if value < node -> go left
if value > node -> go right
if empty spot found -> insert

'''

from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        return Node(val)
    
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)

    return root

def to_list_inorder(root):
    if root is None:
        return []
    return to_list_inorder(root.left) + [root.val] + to_list_inorder(root.right)

def to_list_preorder(root):
    if root is None:
        return []
    return [root.val] + to_list_preorder(root.left) + to_list_preorder(root.right)

def to_list_postorder(root):
    if root is None:
        return[]
    return to_list_postorder(root.left) + to_list_postorder(root.right) + [root.val]

def to_list_levelorder(root):
    if root is None:
        return []
    result = []
    queue = deque([root])

    while queue:    
        node = queue.popleft()
        result.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result

root = Node(5)
insert(root, 3)
insert(root, 7)
insert(root, 6)
insert(root, 8)

print(to_list_levelorder(root))
