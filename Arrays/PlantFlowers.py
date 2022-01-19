"""
605. Can Place Flowers

You have a long flowerbed in which some of the plots are planted, and some are not. 
However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, 
and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 
Constraints:
1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length

"""

def canPlaceFlowers(flowerbed, n):
  """
  1. Test Cases
  [any array], n=0 -> True
  [any array], n > ceil(flowerbed.length/2) -> False
  
  [0,0,0], n=3 -> False
  [0,0,0], n=2 | 1 -> True
  [1,0,0,1,0], n=any -> False
  [1,0,0,0,0,0,1], n=2 -> True
  
  
  2. Plan
  Traversal;
  There are no adjacent flowers in flowerbed. So if flowerbed[i] == 0, if flowerbed[i-1] and flowerbed[i+1] are not 1, we increment flower count and plant flower at i.
  if fb[i] == 1 (or became 1), increment while counter by 2.
  Repeat until flower count reaches n or flowerbed length is reached. When reached, return True. If loop ends withought reaching n, return False.
  
  Edge cases: first element and last element. Only have to check one neighbor.
  """
  
  if n == 0:
    return True
  
  if n > -(-len(flowerbed)//2):
    return False
  
  if len(flowerbed) == 1:
    return flowerbed[0] == 0
  
  
  counter = 0
  i = 0
  
  while counter < n and i < len(flowerbed):
    if flowerbed[i] == 1:
      i += 2
    else:
      if (i == 0 and flowerbed[i+1] == 0) or (i == len(flowerbed)-1 and flowerbed[i-1]==0) or (i != 0 and i != len(flowerbed)-1 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0):
        flowerbed[i] = 1
        i += 2
        counter += 1
      else:
        i += 1
        
  return counter == n