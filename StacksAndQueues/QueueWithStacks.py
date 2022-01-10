class MyQueue:

  def __init__(self):
    self.s1 = []
    self.s2 = []

  def push(self, x: int) -> None:
    self.s1.append(x)
      

  def pop(self) -> int:
    if len(self.s2) == 0:
      while len(self.s1) > 0:
        self.s2.append(self.s1.pop())
    return self.s2.pop()
      

  def peek(self) -> int:
    if len(self.s2) == 0:
      while (len(self.s1)) > 0:
        self.s2.append(self.s1.pop())
    return self.s2[-1]
      

  def empty(self) -> bool:
    return len(self.s1) + len(self.s2) == 0

q = MyQueue()
q.push(1)
q.push(2)
q.push(3)
print(q.peek())
print(q.pop())

print(q.empty())

# q.push(5)
# q.push(6)

# print(q.pop())
# print(q.pop())
# print(q.empty())