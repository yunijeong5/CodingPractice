"""
1. Two Sum

Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.
"""

def twoSum(nums, target):
  """
  Brute force: O(n^2), O(1)
    for each elem, check all elements to its left. if sum == target, return two indices.

  Optimal: O(n), O(n)
    for each elem, record its index and what it needs to reach target in a hashmap.
    if an element if in the hashmap, return current index and the hashmap[myValue].
  """
  numMap = {}

  for i in range(len(nums)):
    cur = nums[i]
    needed = target - cur

    if cur in numMap:
      return [numMap[cur], i]
    else:
      numMap[needed] = i
    
  return None


# print(twoSum([1, 2, 1, 2], 4)) # [1, 3]
# print(twoSum([3, 3, 3], 6)) # [0, 1] | [0, 2] | [1, 2]
# print(twoSum([1, 2, 3], 9)) # None
# print(twoSum([], 3)) # None
# print(twoSum([1], 1)) # None
# print(twoSum([0, 1], 1)) # [0, 1]


#########################################################################################
"""
11. Container With Most Water

You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, 
such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

"""

def mostWater(height):
  """
  area between line i and j = 
      min(height[i], height[j])*(j-i), assuming j >= i

  brute force:
    try all n^2/2 pairs.

  Two pointer:
    from the outermost lines, move the shorter line inward, 
    updating max area on the way.
    repeat until l < r. We move shorter line because inner line may be higher
    and increase max area. Moving longer line doesn't do any good (horizontally and vertially the value only shrinks)
  """
  l = 0
  r = len(height) -1
  maxArea = min(height[l], height[r])*(r-l)

  while l < r:
    if height[l] <= height[r]:
      l += 1
    else:
      r -= 1
    maxArea = max(maxArea, min(height[l], height[r])*(r-l))

  return maxArea

# print(mostWater([1,8,6,2,5,4,8,3,7])) # 49
# print(mostWater([1,1])) # 1
# print(mostWater([1, 7, 7, 1])) # 7


#########################################################################################

"""
42. Trapping Rain Water

Given n non-negative integers representing an elevation map 
where the width of each bar is 1, compute how much water it can trap after raining.
"""

def trapRain(height):
  """
  Two pointer:
    start from left end and right end (l and r) and move shorter side inward.
    keep track of max height of left and right.
    After updating the index of min(l, r), compare height[min(l, r)] to maxHeightL|R
    If maxHeight is less than height[min(l, r)], update max height.
    If maxHeight is not less than height[min(l,r)], add water: water += maxHeight - height[min(l,r)]
  """
  l = 0
  r = len(height) - 1
  water = 0
  maxl = maxr = 0

  while l < r:
    if height[l] <= height[r]:
      if maxl > height[l]:
        water += maxl - height[l]
      else:
        maxl = height[l]
      l += 1
    else:
      if maxr > height[r]:
        water += maxr - height[r]
      else:
        maxr = height[r]
      r -= 1

  return water

# print(trapRain([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
# print(trapRain([4,2,0,3,2,5])) # 9


#########################################################################################

"""
125. Valid Palindrome

A phrase is a palindrome if, after converting all uppercase letters 
into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include 
letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""

def isPalindrome(s):
  """
  Two Pointer
    start from left and right ends, moving inward if s[l] == s[r].
    if at any moment they are not equal, return false.
    repeat until l <= r.
  """
  l = 0
  r = len(s) - 1
  while l <= r:
    if s[l] != s[r]:
      return False
    l += 1
    r -= 1
  return True

# print(isPalindrome('sas')) # True
# print(isPalindrome("")) # True
# print(isPalindrome("qweewq")) # True
# print(isPalindrome("qwedewq")) # True
# print(isPalindrome('skkk')) # False
# print(isPalindrome("qwedewqq")) # False


#########################################################################################

"""
680. Valid Palindrome II

Given a string s, return true 
if the s can be palindrome after deleting at most one character from it.

"""

def almostPalindrome(s):
  """
  Run regular palindrome check. If it passes, return true
  If not, test again on two instances: removing s[l] or s[r].
  If at least one of them passes test, return true.
  """

  l = 0
  r = len(s) - 1

  def substringIsPalindrome(s, l, r):
    while l <= r:
      if s[l] != s[r]:
        return False
      l += 1
      r -= 1
    return True

  while l <= r:
    if s[l] != s[r]:
      return substringIsPalindrome(s, l+1, r) or substringIsPalindrome(s, l, r-1)
    l += 1
    r -= 1
  return True

# print(almostPalindrome("abda")) # True
# print(almostPalindrome("aaaaaab")) # true
# print(almostPalindrome("aa")) # True
# print(almostPalindrome("abcde")) #False
# print(almostPalindrome("abccdeba")) # False


#########################################################################################\

#TRY AGAIN

"""
3. Longest Substring Without Repeating Characters

Given a string s, 
find the length of the longest substring without repeating characters. 

"""
def longestSubstring(s):
  """
  Sliding Window:
    two pointers for left and right end of the window. Start with l = r = 0.
    Also use dictionary to store discovered alphabets and their index.
    If s[r+1] is new, move r to r+1 and update maxLength++.
    If s[r+1] is already seen and seen[s[r+1]] >= l, 
      update maxLength to max(curLength, maxLength)
      l = seen[s[r+1]] + 1
      r += 1
    If s[r+1] is already seen and seen[s[r+1]] < l,
      treat like we found a new letter.
  """
  if len(s) <= 1:
    return len(s)

  l = r = maxlen = 0
  seen = {}

  while r < len(s):
    cur = s[r]

    if cur in seen and seen[cur] >= l:
      l = seen[cur] + 1
    
    seen[cur] = r
    maxlen = max(maxlen, r - l + 1)
    r += 1
  
  return maxlen

print(longestSubstring("abcde")) # 5
print(longestSubstring("aaaaa")) # 1
print(longestSubstring("abcdbef")) # 5
print(longestSubstring('abba')) # 2

#########################################################################################