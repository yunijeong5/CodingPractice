def bubbleSort(arr):
  for i in range(len(arr)):
    for j in range(len(arr)-1):
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]

  return arr

print(bubbleSort([1,3, 4, 1, 5, 6]))


def selectionSort(arr):
  for i in range(len(arr)):
    minIndex = i
    for j in range(i+1, len(arr)):
      if arr[j] < arr[minIndex]:
        minIndex = j

    arr[i], arr[minIndex] = arr[minIndex], arr[i]

  return arr

print(selectionSort([1,3, 4, 1, 5, 6]))


def insertionSort(arr):
  for i in range(1, len(arr)):
    curPos = i
    curVal = arr[i]
    while curPos > 0 and arr[curPos - 1] > curVal:
      arr[curPos] = arr[curPos-1]
      curPos -= 1
    arr[curPos] = curVal
    
  return arr

print(insertionSort([1,3, 4, 1, 5, 6]))

      
        

