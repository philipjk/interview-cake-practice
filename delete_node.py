
class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next = None


a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')

a.next = b
b.next = c


def delete_node(node):

    # Delete the input node from the linked list
    try:
        node.value = node.next.value
        node.next = node.next.next
    except:
        raise Exception('Cannot delete the last item')
