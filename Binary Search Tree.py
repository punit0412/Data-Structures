class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.right_node = None
        self.left_node = None
        # Helpful in removing nodes
        self.parent = parent


class TreeComparator:
    def compare(self, node1, node2):
        # check the base case, these two nodes of a leaf node:
        # node 1 may be none or node 2 may be none:
        if not node1 or not node2:      # Either node is None.
            return node1 == node2       # Compare both nodes (node1 == node2 (node object comparison))

        if node1.data != node2.data:    # Check whether the value is same or not (node value comparison)
            return False

        return self.compare(node1.left_node, node2.left_node) and self.compare(node1.right_node, node2.right_node)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        # BST is empty, so we insert root node
        if self.root is None:
            self.root = Node(data)

        # Else we insert a node according to the value
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        # Inserting the node to the left.
        if data < node.data:
            if node.left_node is None:  # left node is empty
                node.left_node = Node(data,node)
            else:
                self.insert_node(data, node.left_node)      # There is already a node to the left (used Recursion)

        # Inserting a node to the right
        else:
            if node.right_node is None:     # Right node is empty
                node.right_node = Node(data,node)
            else:
                self.insert_node(data, node.right_node)     # There is already a node to the right (used Recursion)

    # Remove the node with the given data in the tree
    def remove(self, data):
        if self.root:
            return self.remove_node(data, self.root)

    def remove_node(self, data, node):
        if node is None:
            return
        if data < node.data:
            # Search for the node in the left-subtree
            return self.remove_node(data, node.left_node)
        elif data > node.data:
            # Search for the node in the right-subtree
            return self.remove_node(data, node.right_node)
        else:
            # We have found the node we would like to remove.
            # There are 3 options

            if node.left_node is None and node.right_node is None:
                # 1) Node is a leaf node
                print(f'Removing the leaf node... {node.data}')
                parent = node.parent
                if parent is not None and parent.left_node == node:
                    # Removing left node
                    parent.left_node = None
                elif parent is not None and parent.right_node == node:
                    # Removing right node
                    parent.right_node = None
                if parent is None:
                    # Removing root node
                    self.root = None

                del node

            elif node.left_node is None and node.right_node:
                # 2) When there is a single child   (RIGHT CHILD)
                print('Removing a node with a single right child...')
                parent = node.parent
                if parent is not None and parent.left_node == node:
                    parent.left_node = node.right_node
                elif parent is not None and parent.right_node == node:
                    parent.right_node = node.right_node

                elif parent is None:
                    self.root = node.right_node

                node.right_node.parent = parent

                del node

            elif node.right_node is None and node.left_node:
                # 2) When there is a single child   (LEFT CHILD)
                parent = node.parent
                if parent is not None:

                    if parent.left_node == node:
                        parent.left_node = node.left_node
                    elif parent.right_node == node:
                        parent.right_node = node.left_node

                else:
                    self.root = node.left_node

                node.right_node.parent = parent     # IN CASE OF ROOT NODE IT WILL BE SET TO NONE

                del node

            else:
                #   REMOVE A NODE WITH 2 CHILDREN
                print("Removing node with two children...")
                predecessor = self.get_predecessor(node.left_node)
                # swap predecessor and node:
                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp

                self.remove_node(data, predecessor)    # data = predecessor.data # Leaf node case or single left child

    def get_predecessor(self, node):
        if node.right_node:
            return self.get_predecessor(node.right_node)

        return node

    # Get the minimum value in the tree.
    def get_min(self):
        if self.root:
            return self.get_min_value(self.root)

    def get_min_value(self, node):
        if node.left_node:
            return self.get_min_value(node.left_node)

        return node.data        # Here node will be leftmost node because each time
        # we call this function we replace node with node.left_node, and we'll get its data.

    # Get maximum value in the tree
    def get_max(self):
        if self.root:
            return self.get_max_value(self.root)

    def get_max_value(self, node):
        if node.right_node:
            return self.get_max_value(node.right_node)

        return node.data        # Here node will be leftmost node because each time
        # we call this function we replace node with node.left_node, and we'll get its data

    """IN ORDER TRAVERSAL"""
    def traverse(self):
        if self.root:
            return self.traverse_in_order(self.root)

    # In order traversal function, O(N) linear running time complexity
    def traverse_in_order(self, node):
        if node.left_node:
            self.traverse_in_order(node.left_node)

        print(node.data)
        if node.right_node:
            self.traverse_in_order(node.right_node)

    def preorder_traversal(self, node):
        print(node.data)

        if node.left_node:
            self.preorder_traversal(node.left_node)

        if node.right_node:
            self.preorder_traversal(node.right_node)

    def postorder_traversal(self, node):
        if node.left_node:
            self.postorder_traversal(node.left_node)
        if node.right_node:
            self.postorder_traversal(node.right_node)

        print(node.data)


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(10)
    bst.insert(8)
    bst.insert(25)
    bst.remove(10)
    bst.insert(54)
    bst.insert(-5)

    bst.traverse()










