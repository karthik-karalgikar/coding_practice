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

    def insertatPosition(self, newNode, position):
        if position == 0:
            self.insertatStart(newNode)
            return
        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition == position:
                previousNode.next = newNode
                newNode.next = currentNode
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition = currentPosition + 1


    def printList(self):
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next

firstNode = Node("Karthik")
linkedList = LinkedList()
linkedList.insertatPosition(firstNode, 0)
secondNode = Node("Kiran")
linkedList.insertatPosition(secondNode,1)
thirdNode = Node("Karalgikar")
linkedList.insertatPosition(thirdNode,2)
linkedList.printList()


'''
TRACING:
here in the function InsertAtPosition, I insert a node at the middle of two 
nodes in a linked list. 
So what I do is, create the function and give it two parameters, the 
node which i'm going to insert(newNode) and the position at which I am going
to insert it(position)

I assign currentNode as the head node and 
the currentPosition as 0
in the while loop, 
I check if the currentPostion value is equal to the position in the function.
If not, then I go to line 17, in which
a variable called previousNode is defined and it is assigned to the 
currentNode. This means that I am storing the value of the currentNode in
the previousNode so as to move the value of currentNode to the next node

After this, i move my current node to the next
and increment the value of currentPosition by 1

I go back to the while loop and now check if the currentPosition is equal 
to the position.
If it is, then the previousNode.next is pointed to the newNode and 
newNode.next is pointed to the currentNode

Pictographical explanation:

|  1  | -> |  2  | -> |  3  | -> null
head
current
curPos = 0
now if I want to insert 2.5 at position 2, then first i have to check 
whether curPos and position are equal. 
0 == 2 -> no
go to line 29
now, the currentNode has to be moved further. Hence,
the previousNode is the currentNode and the currentNode is moved to the next
and the curPos is incremented
So the Linked list looks like this now

|  1  | -> |  2  | -> |  3  | -> null
head 
previous   current
curPos = 1
now check if curPos = position 
1 == 2 -> false
so now, the currentNode is 2 and the previous node is the present current node
and curPos is incremented

|  1  | -> |  2  | -> |  3  | -> null
head
           previous    current
curPos = 2
now, check if curPos == position
2 == 2 -> true
if statement:
    previous.next = newNode
    => 2.next = 2.5
    newNode.next = currentNode
    => 2.5.next = 3

So the final linked list will be 

|  1  | -> |  2  | -> |  2.5  | -> |  3  | -> null
'''
