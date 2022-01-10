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
  
