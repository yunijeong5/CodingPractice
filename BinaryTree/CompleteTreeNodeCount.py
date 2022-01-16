"""
222. Count Complete Tree Nodes

Given the root of a complete binary tree, 
return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, 
is completely filled in a complete binary tree, 
and all nodes in the last level are as far left as possible. 
It can have between 1 and 2^h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

"""

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def countNodes(root):
  if root == None:
    return 0

  def getHeight(cur):
    height = 0
    while cur.left:
      height += 1
      cur = cur.left
    return height

  def nodeExists(indexToFind, height, cur):
    l = 0
    r = 2**height - 1
    count = 0

    while count < height:
      mid = -(-(l+r)//2)
      if indexToFind >= mid: # goal is at the right branch
        cur = cur.right
        l = mid
      else:
        cur = cur.left
        right = mid - 1
      count += 1

    return cur != None


  h = getHeight(root)

  if h == 0:
    return 1

  count = 2**h - 1

  l = 0
  r = count # 2**h - 1

  while l < r:
    mid = -(-(l+r)//2) # integer division round up
    if nodeExists(mid, h, root):
      l = mid
    else:
      r = mid - 1

  return count + l + 1 # same as count + right + 1



root1 = TreeNode(1, TreeNode(2, TreeNode(4, None, None), TreeNode(5, None, None)), TreeNode(3, TreeNode(6, None, None), None))
root2 = None
root3 = TreeNode(1, None, None)

print(countNodes(root1))
print(countNodes(root2))
print(countNodes(root3))