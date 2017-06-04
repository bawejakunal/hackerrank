"""Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None

https://www.hackerrank.com/challenges/is-binary-search-tree
"""

def _check_bst(root, low, high):
    if root is None:
        return True

    if (root.data < low) or (root.data > high):
        return False

    return (_check_bst(root.left, low, root.data - 1) and
            _check_bst(root.right, root.data + 1, high))

def check_binary_search_tree_(root):
    """
    check if a given binary tree is a BST
    """
    if root is None:
        return True
    return _check_bst(root, 0, 10000)
