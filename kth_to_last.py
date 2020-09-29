def kth_to_last_node(k, head_node):
    if k < 1:
        raise ValueError('Impossible to find less than first to last node')
    current = head_node
    kth = head_node
    i = 1

    while current.next:
        if i >= k:
            kth = kth.next
        current = current.next
        i += 1

    if i < k:
        raise ValueError('Theres no kth to last in this list')
    return kth
