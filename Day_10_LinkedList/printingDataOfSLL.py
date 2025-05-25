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
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                else:
                    lastNode = lastNode.next
            lastNode.next = newNode

    def printList(self):
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next

firstNode = Node("Karthik")
linkedList = LinkedList()
linkedList.insert(firstNode)
secondNode = Node("Kiran")
linkedList.insert(secondNode)
thirdNode = Node("Karalgikar")
linkedList.insert(thirdNode)
linkedList.printList()

'''
TRACING:
Here, a function is bring created called printList
A currentNode variable is created and initialised to the head node
It goes through the while loop 
if the currentNode is None(This will be for the last node, so we can ignore 
this for now)
using the print(currentNode.data) we print the data part of the currentNode
and after printing, the currentNode is ,in a way, incremented, i.e.,
the next Node of the linked list will become the currentNode

Now after printing Karthik, Kiran and Karalgikar, the while loop runs again
and checks whether the currentNode is None. It is true in this case
So it breaks out of the loop. 

So the output is:
Karthik
Kiran
Karalgikar
'''
