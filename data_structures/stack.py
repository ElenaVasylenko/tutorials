# Tuple and list are ordered


class Stack:

    def __init__(self, init_stack=None):
        self.stack = init_stack if init_stack else []

    def add(self, item):
        self.stack.append(item)
        return self.stack

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) > 0

    def size(self):
        return len(self.stack)


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class StackLinked:

    # Initializing a stack.
    # Use a dummy node, which is
    # easier for handling edge cases.
    def __init__(self):
        self.value = Node("head")
        self.size = 0

    # String representation of the stack
    def __str__(self):
        cur = self.value.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-3]

    # Get the current size of the stack
    def getSize(self):
        return self.size

    # Check if the stack is empty
    def isEmpty(self):
        return self.size == 0

    # Get the top item of the stack
    def peek(self):
        # Sanitary check to see if we
        # are peeking an empty stack.
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.value.next.value

    # Push a value into the stack.
    def push(self, value):
        node = Node(value)
        node.next = self.value.next
        self.value.next = node
        self.size += 1

    # Remove a value from the stack and return.
    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.value.next
        self.value.next = self.value.next.next
        self.size -= 1
        return remove.value

