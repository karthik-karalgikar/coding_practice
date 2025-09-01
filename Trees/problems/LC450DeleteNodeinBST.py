'''
Node is leaf → just remove it.
Node has 1 child → replace node with child.
Node has 2 children → find inorder successor (min in right subtree), 
                        replace node's value with it, and delete successor.
'''

def delete(root, key):
    if root is None:
        return None

    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        successor = find_min(root.right)
        root.val = successor.val
        root.right = delete(root.right, successor.val)

    return root

def find_min(node):
    while node.left:
        node = node.left
    return node
