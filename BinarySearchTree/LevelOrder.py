"""
102. Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order traversal of
its nodes' values. (i.e., from left to right, level by level).

"""
# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right


def levelOrder(root):
  if root == None:
    return []

  queue = [(root, 1)]
  result = []

  while len(queue) > 0:
    cur = queue.pop(0)
    curNode = cur[0]
    curLevel = cur[1]
    
    if curNode.left != None:
      queue.append((curNode.left, curLevel+1))

    if curNode.right != None:
      queue.append((curNode.right, curLevel+1))

    if len(result) < curLevel: # len(result) is the number of levels we started to cover
      result.append([curNode.val])
    else:
      result[curLevel-1].append(curNode.val)
  
  return result


# without tuple.
def genericLevelOrder(root):
  if root == None:
    return []

  queue = [root]
  result = []

  while len(queue) > 0:
    length = len(queue)
    count = 0
    currentLevelValues = []

    while count < length:
      curNode = queue.pop(0)
      currentLevelValues.append(curNode.val)

      if curNode.left:
        queue.append(curNode.left)
      if curNode.right:
        queue.append(curNode.right)
      
      count += 1
    
    result.append(currentLevelValues)

  return result


root = TreeNode(3, TreeNode(9, None, None), TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)))
root1 = TreeNode(1, None, None)

print(levelOrder(root)) # [[3],[9,20],[15,7]]
print(levelOrder(None)) # []
print(levelOrder(root1)) # [[1]]

print(genericLevelOrder(root)) # [[3],[9,20],[15,7]]
print(genericLevelOrder(None)) # []
print(genericLevelOrder(root1)) # [[1]]