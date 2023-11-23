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

firstNode = Node("Karthik")
linkedList = LinkedList()
linkedList.insert(firstNode)
print(linkedList.head.data)


'''
TRACING:
At first, create a class named Node and define a function with data as it's
parameter. The data part of the node is data(self.data -> here data is the 
attribute and data is the parameter used in the function)

Note: for example, i'm creating a Node and it has the parameter -> Karthik
The parameter of the function is data. So, Karthik stored in the variable data
But for the computer to know that it is data, self.data is used.
That is, self.data = data means seldf.data = "Karthik".

Therefore, a node is created

Now, a class LinkedList is created, and a function is created which 
initialises head as the first node of the linked list. 
It is currently pointing at None. 

Now, to insert elements into the linked list, create the insert function, 
with newNode as its parameter. 
It checks whether the head node is empty or not. If it is, the the head node
is initialied to the newNode

Now for the calling of classes part:
Here an object called the firstNode is created and the Node class is called
with "Karthik" as its parameter.
So therefore, the "Karthik" is stored in the variable named data

Now, an object linkedList is created calling the LinkedList() class.
to insert nodes into the linked list, the insert method is called. 
the insert method takes firstNode as its parameter. 
so if we look at the insert function, its parameter is newNode. So the 
newNode is replaced by firstNode

But to print the data part of firstNode, print in the following way:
print(linkedList.head.data)
here, the data part of the head node is printed. the head node is the 
first replaced by the newNode, which is then replaced by firstNode
So the data part of the firstNode is "Karthik", and that is the value being
printed. 

'''