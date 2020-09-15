class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right


def find_largest(node):
    if node.right:
        return find_largest(node.right)
    else:
        return node


def find_largest_iterative(node):
    while node.right:
        node = node.right
    return node


def find_second_largest(root_node):

    # Find the second largest item in the binary search tree
    largest = find_largest_iterative(root_node)
    if largest.left:
        return find_largest_iterative(largest.left).value
    else:
        parent = root_node
        while parent.right.value != largest.value:
            parent = parent.right
        return parent.value
