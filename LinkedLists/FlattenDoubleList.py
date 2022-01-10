"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
def flatten(head):
  def merge(cur):
    child = cur.child

    while child.next != None:
      child = child.next
    
    if cur.next != None:
      cur.next.prev = child
      child.next = cur.next
    
    cur.next = cur.child
    cur.child.prev = cur
    cur.child = None

  cur = head
  while cur:
    if cur.child != None:
      merge(cur)
    cur = cur.next

  return head
