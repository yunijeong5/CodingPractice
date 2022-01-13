def merge(L, R):
  l = 0
  r = 0
  result = []

  while l < len(L) and r < len(R):
    if L[l] <= R[r]:
      result.append(L[l])
      l += 1
    else:
      result.append(R[r])
      r += 1
  
  # while l < len(L):
  #   result.append(L[l])
  #   l += 1
  if l < len(L):
    result.extend(L[l:])
  
  # while r < len(R):
  #   result.append(R[r])
  #   r += 1
  if r < len(R):
    result.extend(R[r:])

  return result


def mergeSort(arr):
  if len(arr) <= 1:
    return arr

  half = len(arr) // 2
  L = mergeSort(arr[:half])
  R = mergeSort(arr[half:])

  return merge(L, R)


print(mergeSort([1,3, 4, 1, 5, 6, -1, 0, 33, 7]))




def quickSort(arr):
  if len(arr) <= 1:
    return arr
  
  curPos = 0

  for i in range(1, len(arr)):
    if arr[i] <= arr[0]: # @ arr[0]: value less than or equal to pivot
      curPos += 1
      arr[i], arr[curPos] = arr[curPos], arr[i]

  # bring pivot value to correct position
  arr[0], arr[curPos] = arr[curPos], arr[0]

  L = quickSort(arr[:curPos])
  R = quickSort(arr[curPos+1:])

  return L + [arr[curPos]] + R

print(mergeSort([1,3, 4, 1, 5, 6, -1, 0, 33, 7]))