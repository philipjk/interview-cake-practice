def contains_cycle(node):
    if node:
        previous = None
        start = node
        while node.next:
            tmp_next = node.next
            node.next = previous
            previous = node
            node = tmp_next
            if node == start:
                return True

        previous = None
        while node.next:
            tmp_next = node.next
            node.next = previous
            previous = node
            node = tmp_next
        return False
    else:
        return False
