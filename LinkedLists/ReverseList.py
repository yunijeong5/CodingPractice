# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def reverseList(head):
  prev = None
  cur = head
  while cur:
    nxt = cur.next
    cur.next = prev
    prev = cur
    cur = nxt
  return prev


def reverseListRecursive(head):
  return recurHelp(None, head)

def recurHelp(prev, cur):
  if cur == None:
    return prev
  nxt = cur.next 
  cur.next = prev
  return recurHelp(cur, nxt)