"""
assumes that each value in the matrix is unique numbers
arr: 2d array
"""
def dfs(arr):
  if len(arr) == 0:
    return None

  seen = set()
  result = []
  def checkBoundary(i, j):
    return 0 <= i < len(arr) and 0 <= j < len(arr[0])

  def recur(i, j):
    if (i, j) not in seen:
      result.append(arr[i][j])
      seen.add((i, j))

      # up
      if checkBoundary(i-1, j):
        recur(i-1, j)

      # right
      if checkBoundary(i, j+1):
        recur(i, j+1)

      # down
      if checkBoundary(i+1, j):
        recur(i+1, j)

      # left
      if checkBoundary(i, j-1):
        recur(i, j-1)
    
  recur(0, 0)
  return result


arr = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20]]
arr2 = [[1]]
print(dfs(arr))
print(dfs(arr2))




def dfs2(arr):
  # up, right, down, left
  directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
  seen = [[False for i in range(len(arr[0]))] for j in range(len(arr))]
  values = []

  def traverse(matrix, row, col, seen, values):
    # out of bounds or already seen
    if not (0 <= row < len(matrix) and 0 <= col < len(matrix[0]) and not seen[row][col]):
      return

    values.append(matrix[row][col])
    seen[row][col] = True

    for dir in directions:
      traverse(matrix, row+dir[0], col+dir[1], seen, values)

  
  traverse(arr, 0, 0, seen, values)
  return values

print(dfs2(arr))