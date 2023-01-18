class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        currentNode = self.head

        while currentNode:
            print(currentNode.data)
            currentNode = currentNode.next

    def push(self, data):
        newNode = Node(data)

        newNode.next = self.head
        self.head = newNode

    def add_after(self, previous_node, data):
        newNode = Node(data)

        newNode.next = previous_node.next
        previous_node.next = newNode

    def append(self, data):
        newNode = Node(data)

        currentNode = self.head

        while currentNode.next:
            currentNode = currentNode.next

        currentNode.next = newNode

    def remove_element(self, key):
        # If the list is empty
        if self.head is None:
            print("The list is empty")
            return

        # If the key is the current head
        if self.head.data == key:
            self.head = self.head.next
            return

        # Getting the current node
        currentNode = self.head

        while currentNode:
            if currentNode.data == key:
                break

            previousNode = currentNode
            currentNode = currentNode.next

        if currentNode.data is None:
            ("The key doesnt exists inside the list")

        else:
            previousNode.next = currentNode.next


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

linkedList = LinkedList()
linkedList.head = node1
node1.next = node2
node2.next = node3

# Adding elements to the list
linkedList.push(0)
linkedList.add_after(node3, 4)
linkedList.append(5)

linkedList.remove_element(4)

linkedList.print_list()