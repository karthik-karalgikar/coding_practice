'''
Rule - 
if target == node -> found
if target < node -> go left
if target > node -> go right
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def search(root, target):
    if root is None:
        return False
    
    if root.val == target:
        return True
    elif target < root.val:
        return search(root.left, target)
    else:
        return search(root.right, target)

root = Node(5)
root.left = Node(3)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(2)
root.right.right = Node(9)

print(search(root, 9))
