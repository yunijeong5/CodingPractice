"""
98. Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

"""


# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


# inorder recursive
def isValidBSTInorder(root):
  prev = float('-inf')
  def inorderCheck(cur):
    nonlocal prev

    if cur == None:
      return True
    
    if not inorderCheck(cur.left):
      return False

    if cur.val <= prev:
      return False

    prev = cur.val
    return inorderCheck(root.right)

  return inorderCheck(root)
    


# def isValidBST(root):
#   result = True

#   def preorderCheck(cur, minLim, maxLim):
#     nonlocal result
#     if minLim < cur.val < maxLim:
#       if cur.left:
#         preorderCheck(cur.left, minLim, cur.val)
#       if cur.right:
#         preorderCheck(cur.right, cur.val, maxLim)
#     else:
#       result = False
  
#   preorderCheck(root, float('-inf'), float('inf'))
#   return result


def isValidBST(root):
  def preorderCheck(cur, minLim, maxLim):
    if not minLim < cur.val < maxLim:
      return False

    if cur.left:
      if not preorderCheck(cur.left, minLim, cur.val):
        return False
      
    if cur.right:
      if not preorderCheck(cur.right, cur.val, maxLim):
        return False
  
    return True
  
  return preorderCheck(root, float('-inf'), float('inf'))





validTree = TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None))
invalidTree = TreeNode(5, TreeNode(1, None, None), TreeNode(4, TreeNode(3, None, None), TreeNode(6, None, None)))

print(isValidBST(validTree))
print(isValidBST(invalidTree))