"""
104. Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest 
path from the root node down to the farthest leaf node.
"""

# Definition for a binary tree node.
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def maxDepth(root):
  return recurDown(root, 0)

def recurDown(cur, depth):
  if cur == None:
    return depth
  return max(recurDown(cur.left, depth+1), recurDown(cur.right, depth+1))


root = TreeNode(3, TreeNode(9, None, None), TreeNode(20, TreeNode(15, None, None), TreeNode(7, None, None)))

print(maxDepth(root))