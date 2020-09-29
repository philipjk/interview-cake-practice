def reverse(node):
    current_node = node
    previous = None

    while current_node:
        next_node = current_node.next
        current_node.next = previous
        previous = current_node
        current_node = next_node
    return previous
