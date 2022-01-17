class Heap:
  def __init__(self, arr, size=None):
    self.arr = arr
    self.heap_size = size or len(arr)

  def __getitem__(self, key):
    return self.arr[key]

  def __setitem__(self, key, value):
    if len(self.arr)-1 < key:
      self.arr.append(value)
    else:
      self.arr[key] = value
  
  def __len__(self):
    return len(self.arr)

  def __str__(self):
    if self.heap_size == 0:
      return "[]"
    result = []
    for i in range(self.heap_size):
      result.append(A[i])
    return str(result)

def parent(i):
  return (i-1) // 2

def left(i):
  return 2*i + 1

def right(i):
  return 2*i + 2

def maxHeapify(A, i):
  l = left(i)
  r = right(i)
  largest = i # largest of A[i], A[l], A[r]

  if l < A.heap_size and A[l] > A[i]:
    largest = l
  
  if r < A.heap_size and A[r] > A[largest]:
    largest = r

  if largest != i:
    A[i], A[largest] = A[largest], A[i]
    maxHeapify(A, largest)

def buildMaxHeap(A):
  A.heap_size = len(A)
  for i in range(len(A) // 2, -1, -1): # len(A)//2 downto 0
    maxHeapify(A, i)
    print(A.arr)

def heapGetMax(A):
  return A[0]

def heapExtractMax(A):
  if A.heap_size < 1:
    raise Exception("heap underflow")

  maxVal = A[0]
  A[0] = A[A.heap_size - 1]
  A.heap_size = A.heap_size - 1
  maxHeapify(A, 0)
  return maxVal

def heapIncreaseKey(A, i, key):
  if key < A[i]:
    raise Exception("new key is smaller than current value at i")
  A[i] = key
  while i > 0 and A[parent(i)] < A[i]:
    A[i], A[parent(i)] = A[parent(i)], A[i]
    i = parent(i)

def maxHeapInsert(A, key):
  A.heap_size += 1
  A[A.heap_size - 1] = float('-inf')
  heapIncreaseKey(A, A.heap_size - 1, key)

    

A = Heap([1, 2, 3, 4, 5], 5)
buildMaxHeap(A)
print(A)
print('===========')
maxHeapInsert(A, 6)
print(A.arr)
print(heapExtractMax(A))
print(heapExtractMax(A))
print(heapExtractMax(A))
print(heapExtractMax(A))
print(A)