class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def listLength(self):
        length = 0
        currentNode = self.head
        while currentNode is not None:
            length = length + 1
            currentNode = currentNode.next
        return length

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
length = linkedList.listLength()
print(length)
linkedList.printList()