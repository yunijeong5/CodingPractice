def bfs(arr, i, j):
  if len(arr) == 0:
    return None

  def inBoundary(i, j):
    return 0 <= i < len(arr) and 0 <= j < len(arr[0])

  if not inBoundary(i, j):
    return "invalid starting index i, j"

  queue = [(i, j)]
  result = []
  seen = {(i, j)}
  # up, right, down, left
  directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

  while len(queue) > 0:
    cur = queue.pop(0)
    row = cur[0]
    col = cur[1]
    result.append(arr[row][col])

    for dir in directions:
      if (row+dir[0], col+dir[1]) not in seen and inBoundary(row+dir[0], col+dir[1]):
        queue.append((row+dir[0], col+dir[1]))
        seen.add((row+dir[0], col+dir[1]))

  return result



arr = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20]]
arr2 = [[1]]
print(bfs(arr, 2, 2))
print(bfs(arr2, 0, 0))