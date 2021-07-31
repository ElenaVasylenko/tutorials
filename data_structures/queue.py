
class Queue:

    def __init__(self, init_queue=None):
        self._queue = init_queue if init_queue else []

    def add(self, item):
        self._queue.append(item)
        return self._queue

    def pop(self):
        return self._queue.pop(0)

    def is_empty(self):
        return len(self._queue) < 0

    def size(self):
        return len(self._queue)

    def __iter__(self):
        for each in self._queue:
            yield each

    def __repr__(self):
        return "".join(str(self._queue))