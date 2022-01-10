# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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
