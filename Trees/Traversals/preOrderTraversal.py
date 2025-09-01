'''
Preorder traversal -
Root -> Left -> Right
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def preorder(root):
    if root is None:
        return None

    print(root.val, end = " ")
    preorder(root.left)
    preorder(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

preorder(root)

'''
TRACING - 

Tree - 

        1
       / #\#
      2   3
     / \   #\#
    4   5   6

For preorder, the traversal route is root -> left -> right

so it will be 1 -> 2 -> 4 -> 5 -> 3 -> 6 

class Node, defines the tree. 
Currently, it has only the root and the left and right are empty. 

Lines 20 - 25 are called and the above tree is created. 

then, the preorder(root) is called. 

if root is None:
root = 1, not None

print(root.val, end = " ")
Output = 1

preorder(root.left)
root.left = 2

if root is None:
root = 2 (currently)

print(root.val, end = " ")
Output = 1 2

preorder(root.left)
root.left = 4

if root is None:
root = 4 (Currently)

print(root.val, end = " ")
Output = 1 2 4

preorder(root.left)
nothing to left of 4
root.left = None -> return

preorder(root.right)
root.right = None -> return

(backtracks to Node 2)

preoder(root.right)
root.right = 5

if root is None
root = 5 (Currently)

print(root.val, end = " ")
Output = 1 2 4 5

preorder(root.left)
nothing to the left of 5
root.left = None -> return

preoder(root.right)
nothing to the right of 5
root.right = None -> return

(backtracks to Node 1(root))

preorder(root.right)
root.right = 3 

if root is None
root = 3 (Currently)

print(root.val, end = " ")
Output = 1 2 4 5 3

preorder(root.left)
nothing to the left of 3
root.left = None -> return

preorder(root.right)
root.right = 6

if root is None:
root = 6 (Currently)

print(root.val, end = " ")
Output = 1 2 4 5 3 6 

preoder(root.left)
nothing to the left of 6
root.left = None -> return

preorder(root.right)
nothing to the right of 6
root.right = None -> return


'''