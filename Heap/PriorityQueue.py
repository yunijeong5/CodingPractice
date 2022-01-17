class PriorityQueue:
  def __init__(self, comparator=lambda a,b: a > b):
    self._heap = []
    self._comparator = comparator

  def size(self):
    return len(self._heap)

  def isEmpty(self):
    return self.size() == 0

  def peek(self):
    return self._heap[0]

  def push(self, item):
    self._heap.append(item) 
    self.__siftUp()
    return self.size()
    
  def pop(self):
    if self.isEmpty():
      raise Exception("heap underflow")
    if self.size() == 1:
      return self._heap.pop()

    self.__swap(0, self.size()-1)
    popped = self._heap.pop()
    self.__siftDown(0)
    return popped

  def __parent(self, i):
    return (i-1) // 2

  def __left(self, i):
    return 2*i + 1

  def __right(self, i):
    return 2*i + 2

  def __swap(self, i, j):
    self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

  def __compare(self, i, j):
    return self._comparator(self._heap[i], self._heap[j])

  def __siftDown(self, i):
    # assumes that we are descending the first value (index 0) to appropriate place
    l = self.__left(i)
    r = self.__right(i)
    change = i

    if self.size() > l and self.__compare(l, i):
      change = l
    if self.size() > r and self.__compare(r, change):
      change = r
    if change != i:
      self.__swap(i, change)
      self.__siftDown(change)

  def __siftUp(self):
    # assumes that we are trying to make the last elem of heap to bubble up
    curIndex = self.size() - 1

    while curIndex > 0 and self.__compare(curIndex, self.__parent(curIndex)):
      self.__swap(curIndex, self.__parent(curIndex))
      curIndex = self.__parent(curIndex)

  def __str__(self) -> str:
    return str(self._heap)



q = PriorityQueue()
q.push(3)
q.push(4)
q.push(1)
q.push(5)
q.push(2)
print(q)
print(q.pop())
print(q.pop())
print(q.pop())
print(q)



