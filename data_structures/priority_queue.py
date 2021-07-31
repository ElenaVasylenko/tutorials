
class PriorityQueue():
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def isEmpty(self):
        return len(self.queue) == 0

    def insert(self, data):
        self.queue.append(data)

    def delete(self):
        max = 0
        for i in range(len(self.queue)):
            if self.queue[i] > self.queue[max]:
                max = i
        item = self.queue[max]
        self.queue.remove(item)
        return item


if __name__ == '__main__':
    p_queue = PriorityQueue()
    p_queue.insert(12)
    p_queue.insert(1)
    p_queue.insert(14)
    p_queue.insert(7)
    print(p_queue)
    while not p_queue.isEmpty():
        print(p_queue.delete())