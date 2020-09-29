class Stack(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push a new item onto the stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return the last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """Return the last item without removing it"""
        if not self.items:
            return None
        return self.items[-1]

    def __len__(self):
        return len(self.items)


class QueueTwoStacks():

    def __init__(self):
        self.first_stack = Stack()
        self.second_stack = Stack()

    def enqueue(self, item):
        self.first_stack.push(item)

    def dequeue(self):
        if len(self.second_stack):
            return self.second_stack.pop()
        else:
            while len(self.first_stack):
                self.second_stack.push(self.first_stack.pop())
            if not self.second_stack:
                raise IndexError('Cannot dequeue from empty queue')
            return self.second_stack.pop()
