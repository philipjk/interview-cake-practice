class Stack(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []
        self.max_items = []

    def push(self, item):
        """Push a new item onto the stack"""
        self.items.append(item)
        if len(self.items):
            new_max = max(item, self.items[-1])
        else:
            new_max = item
        self.max_items.append(new_max)

    def pop(self):
        """Remove and return the last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None
        self.max_items.pop()
        return self.items.pop()

    def peek(self):
        """Return the last item without removing it"""
        if not self.items:
            return None
        return self.items[-1]

    def get_max(self):
        if not self.max_items:
            return None
        return self.max_items[-1]
