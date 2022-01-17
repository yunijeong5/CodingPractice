def findKthLargest(nums, k):
  if len(nums) == 1:
    return nums[0]
  elif len(nums) == 0:
    return

  curPos = 0

  for i in range(1, len(nums)):
    if nums[i] >= nums[0]:
      curPos += 1
      nums[i], nums[curPos] = nums[curPos], nums[i]

  nums[0], nums[curPos] = nums[curPos], nums[0]

  if curPos == k-1:
    return nums[curPos]
  elif curPos > k-1:
    return findKthLargest(nums[:curPos], k)
  else:
    return findKthLargest(nums[curPos+1:], k-curPos-1)


print(findKthLargest([3,2,3,1,2,4,5,5,6], 4))