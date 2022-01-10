"""
input: sorted number list, target
output: there are two numbers in list that adds up to target Y/N
"""
def hasTwoSum(numbers, target):
  l = 0
  r = len(numbers) - 1
  while l < r:
    s = numbers[l] + numbers[r]
    if s == target:
      return True
    elif s < target:
      l += 1
    else:
      r -= 1
  return False