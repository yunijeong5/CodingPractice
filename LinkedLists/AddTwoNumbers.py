# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
      # Edge cases: 
      # adding two number requires additional digit 
      #   ex) 9 + 9 = 18
      # negative nodes: DNE
      
      # Consider:
      # two lists may have different length
      # When the shorter list has ended, add 0 for the following digits
      
      # idea: recursion
      # stop when both list is empty/None
      # additional digit: If n1 + n2 >= 10, create node with the first digit (ones)
      #   (n1+n2) % 10 and add the second digit (tens) to the next calculation
      #    (n1+n2) // 10 + next_1 + next_2.
      
      
      def recurAdd(lst1, lst2, prev, result):
        if lst1 == lst2 == None:
          if prev != 0:
            result.next = ListNode(prev, None)
          return result
        
        
        n1 = 0
        n2 = 0
        if lst1 != None:
          n1 = lst1.val
          
        if lst2 != None:
          n2 = lst2.val
        
        added = n1+n2
        
        if (added + prev) < 10:
          result.next = ListNode(added + prev, None)
          recurAdd(lst1.next if lst1 else lst1, lst2.next if lst2 else lst2, 0, result.next)
        else:
          result.next = ListNode((added + prev) % 10, None)
          recurAdd(lst1.next if lst1 else lst1, lst2.next if lst2 else lst2, (added + prev) // 10, result.next)
          
          
      result_head = ListNode("dummy", None)
      recurAdd(l1, l2, 0, result_head)
      return result_head.next