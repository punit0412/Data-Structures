class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        return str(self.data)


class LinkedList:

    def __init__(self):
        self.no_of_nodes = 0
        self.head = None

    def insert_at_begining(self, data):
        self.no_of_nodes += 1
        new_node = Node(data)
        # LinkedList is empty
        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_at_end(self,data):
        self.no_of_nodes += 1
        new_node = Node(data)

        if self.head is None :
            self.head = new_node
        else:
            actual_node = self.head
            while actual_node.next_node is not None:
                actual_node = actual_node.next_node

            actual_node.next_node = new_node

    def remove(self,data):
        # the list is empty
        if self.head is None:
            return

        actual_node = self.head

        previous_node = None

        while actual_node is not None and actual_node.data != data :
            previous_node = actual_node
            actual_node = actual_node.next_node
        # search miss
        if actual_node is None:
            return

        # update the references
        # the head mode is the one we want to remove
        if previous_node is None:
            self.head = actual_node.next_node
        else:
            # remove an internal node
            previous_node.next_node = actual_node.next_node

    def size_of_linkedlist(self):
        return self.no_of_nodes

    def traverse(self):
        actual_node = self.head

        while actual_node is not None:
            print(actual_node)
            actual_node = actual_node.next_node


linked_list = LinkedList()
linked_list.insert_at_begining(20)
linked_list.insert_at_begining(50)
linked_list.insert_at_begining('punit')
linked_list.insert_at_begining(280)
linked_list.traverse()
linked_list.remove(50)
linked_list.traverse()

