"""
Given an array of integers nums sorted in non-decreasing order, 
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

"""
def binarySearch(nums, l, r, target):  
  while l <= r:
    mid = (l+r)//2
    found = nums[mid]
    
    if found == target:
      return mid
    elif found < target:
      l = mid+1
    else:
      r = mid-1
  
  return -1


def searchRange(nums, target):
  if len(nums) == 0:
    return [-1, -1]
    
  found = binarySearch(nums, 0, len(nums)-1, target)
  
  if found > -1: # target exists in nums
    tempL = tempR = l = r = found
    
    while tempL > -1:
      l = tempL
      tempL = binarySearch(nums, 0, l-1, target)
        
    while tempR > -1:
      r = tempR
      tempR = binarySearch(nums, r+1, len(nums)-1, target)
    
    return [l, r]
  
  return [-1, -1]

print(searchRange([], 5)) # [-1. -1]
print(searchRange([1,2,3,3,4], 9)) # [-1, -1]
print(searchRange([1,2,3,3,4], 3)) # [2, 3]
print(searchRange([1,2,3,4], 1)) # [0, 0]
print(searchRange([1,1,1,1,1], 1)) # [0, 4]
        