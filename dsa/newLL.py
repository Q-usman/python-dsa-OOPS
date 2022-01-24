class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
    def Traverse(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
    def insertAtEnd(self,data):
        newNode = Node(data)
        prevNode = self.head
        if self.head == None:
            self.head = newNode
        else:
            while prevNode.next != None:
                prevNode = prevNode.next
            prevNode.next = newNode
    def insertAtStart(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
    def deleteAtStart(self):
        pass
    def deleteAtEnd(self):
        pass

l = linkedlist()
l.insertAtEnd(20)
l.insertAtEnd(30)
l.insertAtStart(1)
l.Traverse()
# l.head = Node(20)
# l.head.next = Node(30)
# l.head.next.next = Node(40)
# l.Traverse()

