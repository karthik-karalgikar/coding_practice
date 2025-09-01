'''
LevelOrder Traversal:
Left -> Right (breadth first search)
'''

from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def levelOrder(root):
    if root is None:
        return 
    
    queue = deque([root])

    while queue:
        node = queue.popleft()
        print(node.val, end = " ")

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

levelOrder(root)

'''
TRACING - 

Tree - 

        1
       / \#
      2   3
     / \   \#
    4   5   6

For preorder, the traversal route is left -> right

so it will be 1 -> 2 -> 3 -> 4 -> 5 -> 6 

class Node, defines the tree. 
Currently, it has only the root and the left and right are empty. 

Lines 29 - 34 are called and the above tree is created. 

then levelOrder(root) is called

initially root is 1

if root is None:
root = 1, Not None

queue = deque([root])

deque = double-ended queue is like a list but optimised for fast appends and pops from both ends (O(1) time)
queue = deque([1])

while queue:
    node = queue.popleft() (left most element is removed from the queue)
    queue = [] (1 is removed)
    print(node.val, end = " ")

    node.val = 1
    Current Output = 1

    if node.left: -> left of node(1) is 2
        queue.append(node.left)
        queue = [2]

    if node.right; -> left of node(1) is 3
        queue.append(node.right)
        queue = [2, 3]

    ----------------------------------------------------
    node = queue.popleft() (queue = [2, 3])
    queue = [3] (2 is removed)
    print(node.val, end = " ")

    node.val = 2
    Current Output = 1 2

    if node.left: -> left of node(2) is 4
        queue.append(node.left)
        queue = [3, 4]

    if node.right: -> right of node(2) is 5
        queue.append(node.right)
        queue = [3, 4, 5]
    
    ---------------------------------------------------
    node  = queue.popleft() (queue = [3, 4, 5])
    queue = [4, 5]
    print(node.val, end = " ")

    node.val = 3
    Current Output = 1 2 3

    if node.left: -> left of node(3) is nothing, so it will not go inside if statement

    if node.right: -> right of node(3) is 6
        queue.append(node.right)
        queue = [4, 5, 6]

    ----------------------------------------------------
    node = queue.popleft() (queue = [4, 5, 6])
    queue = [5, 6]
    print(node.val, end = " ")

    node.val = 4
    Current Output = 1 2 3 4

    if node.left: -> left of node(4) is nothing, so it will not go inside if statement

    if node.right: -> right of node(4) is nothing

    ----------------------------------------------------
    node = queue.popleft() (queue = [5, 6])
    queue = [6]
    print(node.val, end = " ")

    node.val = 5
    Current Output = 1 2 3 4 5

    if node.left: -> left of node(5) is nothing

    if node.right: -> left of node(5) is nothing

    ----------------------------------------------------
    node = queue.popleft() (queue = [6])
    queue = []
    print(node.val, end = " ")

    node.val = 6
    Current Output = 1 2 3 4 5 6

    if node.left: -> left of node(6) is nothing

    if node.right: -> left of node(6) is nothing

    ----------------------------------------------------
    queue is empty now, so out of while loop

    
Output = 1 2 3 4 5 6
      

'''