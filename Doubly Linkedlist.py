class Node:
    def __init__(self,data):
        self.data = data
        self.next_node = None
        self.previous_node = None

class DoublyLinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    # this operation insert item at the end of linkedlist
    # so we have to manipulate the tail node in O(1) running time

    def insert(self,data):
        new_node = Node(data)

        # linkedlist is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # there is at least 1 item in the linked list
        # we keep inserting the items at the end of linked list
        else:
            new_node.previous_node = self.tail
            self.tail.next_node = new_node
            self.tail = new_node
    # we can traverse a doubly linked list in both direction

    def traverse_forward(self):

        actual_node = self.head

        while actual_node is not None:
            print("%d" % actual_node.data)
            actual_node = actual_node.next_node

    def traverse_backward(self):
        actual_node = self.tail

        while actual_node is not None:
            print("%d" % actual_node.data)
            actual_node = actual_node.previous_node


linkedlist = DoublyLinkedlist()
linkedlist.insert(1)
linkedlist.insert(2)
linkedlist.insert(3)
linkedlist.insert(5)
linkedlist.traverse_forward()