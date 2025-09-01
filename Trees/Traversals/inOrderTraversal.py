'''
Inorder Traversal : 
Left -> Root -> Right
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder(root):
    if root is None:
        return 
    
    inorder(root.left)
    print(root.val, end = " ")
    inorder(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

inorder(root)

'''
TRACING - 

Tree - 

        1
       / \#
      2   3
     / \   \#
    4   5   6

For inorder, the traversal route is left -> root -> right

so it will be = 4 -> 2 -> 5 -> 1 -> 3 -> 6

class Node, defines the tree. 
Currently, it has only the root and the left and right are empty. 

Lines 20 - 25 are called and the above tree is created. 

then, the inorder(root) is called. 

Initially, the root is 1

if root is None:
root = 1, Not None

inorder(root.left)
root.left = 2

if root is None:
root = 2, Not None

inorder(root.left)
root.left = 4

if root is None:
root = 4, Not None

inorder(root.left)
nothing to the left of 4
root.left = None -> return

if root is None:
None returned

print(root.val, end = " ")
Output = 4

inorder(root.right)
nothing to the right of 4
root.right = None -> return

if root is None: 
None returned

(backtrack to 2)

print(root.val, end = " ")
Output = 4 2

inorder(root.right)
root.right = 5

if root is None:
root 5, Not None

print(root.val, end = " ")
Output = 4 2 5

inorder(root.right)
nothing to right to 5
root.right = None -> return

if root is None:
None returned

(backtrck to 1)

print(root.val, end = " ")
Output = 4 2 5 1

inorder(root.right)
root.right = 3

if root is None:
root = 3, Not None

inorder(root.left)
nothing to the left of 3
root.left = None -> return

if root is None:
None returned

print(root.val, end = " ")
Output = 4 2 5 1 3

inorder(root.right)
root.right = 6

if root is None:
root = 6, Not None

inorder(root.left)
nothing to the left of 6
root.left = None -> return

if root is None:
None returned

print(root.val, end = " ")
Output = 4 2 5 1 3 6

inorder(root.right)
nothing to the right of 6
root.right = None -> return
'''