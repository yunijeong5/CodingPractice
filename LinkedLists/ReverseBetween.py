"""
92. Reverse Linked List II

Given the head of a singly linked list and two integers left and right 
where left <= right, reverse the nodes of the list from position left to 
position right, and return the reversed list.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def reverseBetween(head, l, r):
  curPos = 1
  curNode = head
  start = head

  while curPos < l:
    start = curNode
    curNode = curNode.next
    curPos += 1
  
  listSoFar = None
  tail = curNode

  while curPos <= r:
    nxt = curNode.next 
    curNode.next = listSoFar
    listSoFar = curNode
    curNode = nxt
  
  start.next = listSoFar
  tail.next = curNode

  if l == 1:
    return listSoFar
  else:
    return head
  
