
class Queue:

    def __init__(self, init_queue=None):
        self.queue = init_queue if init_queue else []

    def add(self, item):
        self.queue.append(item)
        return self.queue

    def pop(self):
        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) > 0

    def size(self):
        return len(self.queue)