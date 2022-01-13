"""
Breadth first search of a binary search tree, where each node has left and right subtrees
For demo purpose, it traverses tree and returns node values as a list.
"""

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def BFS(root):
  if root == None:
    return []

  result = []
  queue = [root]

  while len(queue) > 0:
    cur = queue.pop(0)
    result.append(cur.val)

    if cur.left:
      queue.append(cur.left)
    if cur.right:
      queue.append(cur.right)

  return result

root = TreeNode(3, TreeNode(9, None, TreeNode(10, None, None)), TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)))

print(BFS(root))
    

