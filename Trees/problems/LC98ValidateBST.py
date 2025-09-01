'''
Rule - 
left subtree values < node
right subtree values > node
'''

def is_bst(root, left = float("-inf"), right = float("-inf")):
    if root is None:
        return True
    if not (left < root.val < right):
        return False
    return is_bst(root.left, left, root.val) and is_bst(root.right, root.val, right)