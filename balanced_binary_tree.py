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


tree = BinaryTreeNode(1)
left = tree.insert_left(2)
right = tree.insert_right(4)
left.insert_left(3)
left_right = left.insert_right(7)
left_right.insert_right(8)
right_right = right.insert_right(5)
right_right_right = right_right.insert_right(6)
right_right_right.insert_right(9)


def DFS(parent_node, value):
    # find if value is in tree
    if parent_node.value == value:
        return True
    children = [child for child in [parent_node.left, parent_node.right]
                if child]
    for child in children:
        if DFS(child, value):
            return True
    return False


print(DFS(tree, 11))


def BFS(nodes, value):
    children = [l_or_r
                for l_or_r in [node.right, node.left]
                for node in nodes]
    for node in nodes:
        if node.value == value:
            return True
    BFS(children)


# print(BFS([tree], 6))


def is_balanced(tree_root):

    # Determine if the tree is superbalanced
    delta = 0
    return True
