'''
Postorder traversal: 
Left -> Right -> Root
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def postorder(root):
    if root is None:
        return 
    
    postorder(root.left)
    postorder(root.right)
    print(root.val, end = " ")

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

postorder(root)

'''
TRACING - 

Tree - 

        1
       / #\#
      2   3
     / \   #\#
    4   5   6

For inorder, the traversal route is left -> root -> right

so it will be = 4 -> 5 -> 2 -> 6 -> 3 -> 1

class Node, defines the tree. 
Currently, it has only the root and the left and right are empty. 

Lines 20 - 25 are called and the above tree is created. 

then, the postorder(root) is called. 

Initially, root is 1

if root is None:
root = 1, Not None

postorder(root.left)
root.left = 2

if root is None:
root = 2, Not None

postorder(root.left)
root.left = 4

if root is None:
root = 4, Not None

postorder(root.left)
nothing to the left of 4
root.left = None -> return

if root is None:
None returned

postorder(root.right)
nothing to the right of 4
root.right = None -> return

if root is None:
None returned

print(root.val, end = " ")
Output = 4

(backtrack to 2)

if root is None:
root = 2, Not None

postorder(root.right)
root.right = 5

if root is None:
root = 5, Not None

postorder(root.left)
nothing to the left of 5
root.left = None -> return

if root is None:
None returned

postorder(root.right)
nothing to the right of 5
root.right = None -> return

if root is None:
None returned

print(root.val, end = " ")
Output = 4 5

(backtrack to 2)

print(root.val, end = " ")
Output = 4 5 2

(backtrack to 1)

root = 1

postorder(root.right)
root.right = 3

if root is None:
root = 3, Not None

postorder(root.left)
nothing to the left of 3
root.left = None -> return

if root is None:
None returned

postorder(root.right)
root.right = 6

if root is None:
root = 6, Not None

postorder(root.left)
nothing to the left of 6
root.left = None -> return

if root is None
None returned

postorder(root.right)
nothing to the right of 6
root.right = None -> return

if root is None
None returned

print(root.val, end = " ")
Output = 4 5 2 6

(backtrack to 3)

print(root.val, end = " ")
Output = 4 5 2 6 3

(backtrack to 1)

print(root.val, end = " ")
Output = 4 5 2 6 3 1

'''