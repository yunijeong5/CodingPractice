def binarySearch(arr, key): # T: O(lg n), S: O(1)
  # arr is sorted
  # returns the index of key in arr; if DNE, return None
  
  l = 0
  r = len(arr)-1

  while l <= r:
    mid = (r+l) // 2  # lower median
    found = arr[mid]

    if found == key:
      return mid
    elif found < key:
      l = mid + 1
    else:
      r = mid - 1

  return None


a = [1, 2, 2, 2, 3]
b = []
print(binarySearch(a, 2))
print(binarySearch(b, 80))
