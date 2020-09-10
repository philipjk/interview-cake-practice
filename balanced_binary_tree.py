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
    # find if a value is in the tree with DFS (recursive)
    if parent_node.value == value:
        return True
    children = [child for child in [parent_node.left, parent_node.right]
                if child]
    for child in children:
        if DFS(child, value):
            return True
    return False


def BFS(nodes, value):
    # find if a value is in the tree with BFS (recursive)
    if not nodes:
        return False
    children = []
    for node in nodes:
        if node.value == value:
            return True
        if node.right:
            children.append(node.right)
        if node.left:
            children.append(node.left)

    if BFS(children, value):
        return True

    return False


# print(DFS(tree, 11))
# print(BFS([tree], 11))
tree = BinaryTreeNode(3)
left = tree.insert_left(4)
right = tree.insert_right(2)


def min_max_depth(node, layers):
    # determine min and max depths with DFS (recursive)
    layers += 1
    children = [n for n in [node.left, node.right] if n]
    if not len(children):
        return layers, layers
    depths = []
    for n in children:
        result = min_max_depth(n, layers)
        depths.append(result[0])
        depths.append(result[1])
    return max(depths), min(depths)


def is_balanced(tree_root):

    # Determine if the tree is superbalanced

    depth = 1
    parent_nodes = [tree_root]
    leaf_depths = []
    while len(parent_nodes):
        children_nodes = []
        for node in parent_nodes:
            for n in [node.left, node.right]:
                if n:
                    children_nodes.append(n)
            if not (node.right or node.left):
                leaf_depths.append(depth)
        parent_nodes = children_nodes
        depth += 1
    if max(leaf_depths) - min(leaf_depths) > 1:
        return False
    else:
        return True


tree = BinaryTreeNode(1)
left = tree.insert_left(2)
left_left = left.insert_left(3)
left.insert_right(4)
left_left.insert_left(5)
left_left.insert_right(6)
right = tree.insert_right(7)
right_right = right.insert_right(8)
right_right_right = right_right.insert_right(9)
right_right_right.insert_right(10)

print(is_balanced(tree))
