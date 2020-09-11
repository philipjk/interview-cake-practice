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
left_left = left.insert_left(3)
left.insert_right(4)
left_left.insert_left(5)
left_left.insert_right(6)
right = tree.insert_right(7)
right_right = right.insert_right(8)
right_right_right = right_right.insert_right(9)
right_right_right.insert_right(10)


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


def iterative_DFS(parent_node, value):
    # find if a value is in the tree with DFS (iterative)
    stack = [parent_node]
    while len(stack) > 0:
        node = stack.pop()
        if node.value == value:
            return True
        children = [n for n in [node.right, node.left] if n]
        if len(children):
            for child in children:
                stack.append(child)
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


def iterative_BFS(tree_root, value):
    # find if a value is in the tree with BFS (iterative)
    queue = [tree_root]
    i = 0
    while i < len(queue):
        node = queue[i]
        i += 1
        if node.value == value:
            return True
        for n in [node.right, node.left]:
            if n:
                queue.append(n)
    return False


print(iterative_BFS(tree, 1))
print(iterative_DFS(tree, 1))
# print(DFS(tree, 11))
# print(BFS([tree], 11))


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


def is_balanced(tree_root, value):

    # Determine if the tree is superbalanced
    stack = [(tree_root, 1)]
    depths = []
    while len(stack):
        node, depth = stack.pop()
        children = [n for n in [node.right, node.left] if n]
        if len(children):
            for child in children:
                stack.append((child, depth + 1))
        else:
            max_depth = max(depths + [depth])
            min_depth = min(depths + [depth])
            depths = [max_depth, min_depth]

    if max_depth - min_depth > 1:
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

# print(is_balanced(tree))
