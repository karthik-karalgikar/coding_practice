class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insertatStart(self, newNode):
        if self.head is None:
            self.head = newNode

        else:
            tempNode = self.head
            self.head = newNode
            self.head.next = tempNode

    def printList(self):
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next

firstNode = Node("Karthik")
linkedList = LinkedList()
linkedList.insertatStart(firstNode)
secondNode = Node("Kiran")
linkedList.insertatStart(secondNode)
thirdNode = Node("Karalgikar")
linkedList.insertatStart(thirdNode)
linkedList.printList()

'''
TRACING:
here, at first a temporary node is taken. 
that node is assigned to the current head node. 
now the head node is assigned to the new node
and the next of the now head node is then connected to the then head node

for example, 
1 -> 2 -> 3 -> was the linked list and I want to insert 0 at the beginning.

Here, 1 is the head node
so a new temp node is assigned to the head node(1)
and then the new head node is assigned to 0(newnode)
and now the new head node's next is pointed to the temp node(1)

pictographically, 
|  1  | -> |  2 | -> | 3 | -> null
  head
tempnode

|  0  | -> | 1 | -> | 2 | -> | 3 | -> null
 head     tempnode

 
'''