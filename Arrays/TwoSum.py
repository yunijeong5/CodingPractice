def twoSum(nums, target):
  """
  return two indices of elements in nums, such that they add up to target
  output is a list

  Exactly one solution exists
  """

  # key: numToFind, value: index that needs this numToFind
  numsMap = {}

  for i in range(len(nums)):
    if nums[i] in numsMap:
      return [numsMap[nums[i]], i]
    else:
      numsMap[target - nums[i]] = i


print(twoSum([0, -1, 1, 2], 3))