import heapq


class PriorityQueue:

     def __init__(self):
          self._data = []

     def push(self, item, priority):
          heapq.heappush(self._data, (-priority, item))

     def pop(self):
          if self._data:
               return heapq.heappop(self._data)[-1]

     def is_empty(self):
          return not self._data



customers = PriorityQueue()
customers.push("Harry", 11)
customers.push("Charles", 2)
customers.push("Riya",3)
customers.push("Stacy", 4)

while not customers.is_empty():
     print(customers.pop())