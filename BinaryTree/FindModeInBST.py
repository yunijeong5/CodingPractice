"""
501. Find Mode in Binary Search Tree

Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently ocnodered element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.

"""
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def findMode(root):
  mode = []
  freq_max = 1 # aaah this was the missing piece!!!
  last = float('inf')
  freq = 0
  
  def inorder(node):
    nonlocal mode, freq_max, last, freq
    
    if node.left:
      inorder(node.left)
      
    if last == node.val:
      freq += 1
    else:
      if freq > freq_max: 
        freq_max, mode = freq, [last]

      elif freq == freq_max:
        mode.append(last)

      freq = 1
      last = node.val
      
    if node.right:
      inorder(node.right)
      
  inorder(root)

  # last element does not get compared as last
  if freq > freq_max:
    return [last]
  elif freq == freq_max:
    mode.append(last)

  return mode



root1 = TreeNode(5, TreeNode(3, TreeNode(3, None, None), None), TreeNode(5, TreeNode(6, None, None), TreeNode(7, None, None)))
root2 = TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None))

print(findMode(root1))
print(findMode(root2))