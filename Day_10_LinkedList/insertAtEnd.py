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

firstNode = Node("Karthik")
linkedList = LinkedList()
linkedList.insert(firstNode)
secondNode = Node("Kiran")
linkedList.insert(secondNode)
thirdNode = Node("Karalgikar")
linkedList.insert(thirdNode)


'''
TRACING:
in the else statement:
the lastNode is initialised to the head Node. 
Here the lastNode and the head node are pointed to the same node
Then it goes into the while loop and checks the if statement.
If the linked lits is Karthik -> None, 
then, here the head node and the LastNode next part is None
So, the if statement is true and it breaks out of the loop

So now, the lastNode.next becomes the newNode

The linked list is as follows:
Kartihk -> Kiran -> None

If another Node is to be inserted:
Steps:
1) Head not empty
2) lastNOde = head
3) lastNode.next = None  ?
   -> No[For the node Karthik]
4) goes to else statement:
   -> lastNode = lastNode.next, i.e., it goes to the next Node
5) lastNode = Kiran
6) lastnode.next = None  ?
    -> Yes [For "Kiran"]
7) breaks out of loop
8) lastNode.next = newNode, => newnNode = 'Karalgikar'

Linked List -> Karthik -> Kiran -> Karalgikar -> None
'''