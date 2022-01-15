"""
199. Binary Tree Right Side View

Given the root of a binary tree, imagine yourself standing on the
right side of it, return the values of the nodes you can see ordered from top to bottom.

"""
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def rightSideViewBFS(root):
  if root == None:
    return root

  queue = [(root, 1)]
  levels = []

  while len(queue) > 0:
    cur = queue.pop(0)
    curNode = cur[0]
    curLevel = cur[1]
    
    if curNode.left:
      queue.append((curNode.left, curLevel+1))
    if curNode.right:
      queue.append((curNode.right, curLevel+1))

    if len(levels) < curLevel:
      levels.append([curNode.val])
    else:
      levels[curLevel-1].append(curNode.val)
  
  result = []
  for level in levels:
    result.append(level[-1])

  return result


def genericRightSideViewBFS(root):
  if root == None:
    return root

  queue = [root]
  result = []

  while len(queue) > 0:
    levelSize = len(queue)
    count = 1

    while count <= levelSize:
      curNode = queue.pop(0)

      if count == levelSize:
        result.append(curNode.val)

      if curNode.left:
        queue.append(curNode.left)
      if curNode.right:
        queue.append(curNode.right)
      
      count += 1

  return result
  

def rightSideViewDFS(root):
  if root == None:
    return root

  result = []

  def traverseNRL(cur, level):
    if level > len(result):
      result.append(cur.val)
    if cur.right:
      traverseNRL(cur.right, level+1)
    if cur.left:
      traverseNRL(cur.left, level+1)

  traverseNRL(root, 1)

  return result
    
    

root = TreeNode(9, TreeNode(4, TreeNode(1, None, None), TreeNode(6, None, None)), TreeNode(20, TreeNode(15, None, None), TreeNode(170, None, None)))
root2 = TreeNode(1, TreeNode(2, TreeNode(4, None, TreeNode(7, TreeNode(8, None, None), None)), TreeNode(5, None, None)), TreeNode(3, None, TreeNode(6, None, None)))

# print(rightSideViewBFS(root))
# print(rightSideViewBFS(root2))
# print(genericRightSideViewBFS(root))
# print(genericRightSideViewBFS(root2))
print(rightSideViewDFS(root))
print(rightSideViewDFS(root2))