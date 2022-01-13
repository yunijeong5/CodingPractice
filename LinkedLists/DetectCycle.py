"""
142. Linked List Cycle II

Given the head of a linked list, return the node where the cycle begins. 
If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that 
can be reached again by continuously following the next pointer. 
Internally, pos is used to denote the index of the node that tail's next 
pointer is connected to (0-indexed). It is -1 if there is no cycle. 
Note that pos is not passed as a parameter.

Do not modify the linked list.


"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Brute Force: T --> O(n), S --> O(n)
def detectCycle(head):
  cur = head
  seen = set()

  while cur:
    if cur in seen:
      return cur
    seen.add(cur)
    cur = cur.next
  return None

# Two Pointer | Floyd's Tortoise and Hare: T --> O(n), S --> O(1)
def detectCycle(head):
  turtle = head
  bunny = head

  while bunny and bunny.next:
    turtle = turtle.next
    bunny = bunny.next.next

    if turtle == bunny:
      bunny = head

      while turtle != bunny:
        turtle = turtle.next
        bunny = bunny.next
      return bunny

  return None

  # Time is O(n) since turtle does not loop. <-- why?
