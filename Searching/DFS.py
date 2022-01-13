"""
Depth first search of a binary search tree, where each node has left and right subtrees
"""

class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right


# Preorder: root, left, right
def DFS_Preorder(root):
  if root == None:
    return root
  return traversePreorder(root, [])

def traversePreorder(cur, result):
  result.append(cur.val)
  if cur.left:
    traversePreorder(cur.left, result)
  if cur.right:
    traversePreorder(cur.right, result)
  return result


# Inorder: left, root, right
def DFS_Inorder(root):
  if root == None:
    return root
  return traverseInorder(root, [])

def traverseInorder(cur, result):
  if cur.left:
    traverseInorder(cur.left, result)
  result.append(cur.val)
  if cur.right:
    traverseInorder(cur.right, result)
  return result


# left, right, root
def DFS_Postorder(root):
  if root == None:
    return root
  return traversePostorder(root, [])

def traversePostorder(cur, result):
  if cur.left:
    traversePostorder(cur.left, result)
  if cur.right:
    traversePostorder(cur.right, result)
  result.append(cur.val)
  return result
  

root = TreeNode(9, TreeNode(4, TreeNode(1, None, None), TreeNode(6, None, None)), TreeNode(20, TreeNode(15, None, None), TreeNode(170, None, None)))

print('inorder', DFS_Inorder(root))
print('postorder', DFS_Postorder(root))
print('preorder', DFS_Preorder(root))

#          9
#       /     \
#     4       20
#   /   \    /  \
# 1      6  15  170

