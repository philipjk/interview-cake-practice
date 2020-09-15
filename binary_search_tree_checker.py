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


"""
def is_binary_search_tree(node,
                          left_bound=-float('inf'),
                          right_bound=float('inf')):
    # recursive DFS to check if a binary tree is a BST

    if left_bound <= node.value <= right_bound:
        right_hand = True
        if node.right:
            right_hand = is_binary_search_tree(node.right,
                                               node.value,
                                               right_bound)
        left_hand = True
        if node.left:
            left_hand = is_binary_search_tree(node.left,
                                              left_bound,
                                              node.value)
        return right_hand*left_hand
    else:
        return False"""


def is_binary_search_tree(root_node,
                          left_bound=-float('inf'),
                          right_bound=float('inf')):
    stack = [(root_node, left_bound, right_bound)]
    while len(stack) > 0:
        node, left_bound, right_bound = stack.pop()
        if not (left_bound <= node.value <= right_bound):
            return False
        if node.right:
            stack.append((node.right, node.value, right_bound))
        if node.left:
            stack.append((node.left, left_bound, node.value))
    return True
