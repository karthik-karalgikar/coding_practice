class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert(self, newNode):
        if self.head is None:
            self.head = newNode

        else:
            self.head.next = newNode

firstNode = Node("Karthik")
linkedList = LinkedList()
linkedList.insert(firstNode)
secondNode = Node("Kiran")
linkedList.insert(secondNode)

'''
TRACING:
Here, in the else statememt:
the next node is being added to the head node by the 
self.head.next = newNode line
here, the next part of the linked list is pointing to the newNode and hence
a newNode is added to the SLL.

So the output will be like: Karthik -> Kiran -> None

But this is node the ideal solution. Because if I want to insert another node,
then the node will be inserted to the next of the head node and not to the
next of the node which is at the last
for ex:
    Karthik -> Kiran -> None will become
    Karthik -> Kiran
            -> Karalgikar(Not like this exactly.)

        

'''

