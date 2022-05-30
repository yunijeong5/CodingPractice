"""
160. Intersection of Two Linked Lists

Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
If the two linked lists have no intersection at all, return null.

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode(headA: ListNode, headB: ListNode):
  
  def getLength(lh):
    count = 0
    while lh:
      count += 1
      lh = lh.next
    return count
  
  Alen = getLength(headA)
  Blen = getLength(headB)
  
  if Alen > Blen:
    longlist = headA
    shortlist = headB
    longlen = Alen
    shortlen = Blen
  else:
    longlist = headB
    shortlist = headA
    longlen = Blen
    shortlen = Alen
    
  while longlen > shortlen:
    longlen -= 1
    longlist = longlist.next
    
  while longlist and shortlist:
    if longlist == shortlist:
      return longlist
    longlist = longlist.next
    shortlist = shortlist.next
    
  return None