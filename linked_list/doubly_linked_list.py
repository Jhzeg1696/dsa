class Node:
    def __init__(self, data):
        self.previous = None
        self.data = data
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.firstNode = None
        self.lastNode = None

    def append(self, data):
        if self.lastNode is None:
            self.head = Node(data)
            self.lastNode = self.head

        else:
            newNode = Node(data)

            self.lastNode.next = newNode
            newNode.previous = self.lastNode
            newNode.next = None
            self.lastNode = newNode

    def display(self, Type):
        if Type == "Left_to_right":
            currentNode = self.head

            while currentNode:
                print(currentNode.data, end=" ")
                currentNode = currentNode.next

            print()

        else:
            currentNode = self.lastNode

            while currentNode:
                print(currentNode.data, end=" ")
                currentNode = currentNode.previous

            print()


doublyLinkedList = DoublyLinkedList()
doublyLinkedList.append(1)
doublyLinkedList.append(2)
doublyLinkedList.append(3)
doublyLinkedList.append(4)
doublyLinkedList.append(5)

doublyLinkedList.display("Left_to_right")
doublyLinkedList.display("Right_to_left")