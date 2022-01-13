"""
1. Two Sum

Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.
"""

def twoSum(nums, target):

  # key: numToFind, value: index that needs this numToFind
  numsMap = {}

  for i in range(len(nums)):
    if nums[i] in numsMap:
      return [numsMap[nums[i]], i]
    else:
      numsMap[target - nums[i]] = i


print(twoSum([0, -1, 1, 2], 3))