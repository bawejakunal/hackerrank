# https://www.hackerrank.com/challenges/ctci-is-binary-search-tree

""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def _checkBST_(root, minVal, maxVal):
    if root is None:
        return True
    if (root.data < minVal) or (root.data > maxVal):
            return False
    return _checkBST_(root.left, minVal, root.data-1) and _checkBST_(root.right, root.data + 1, maxVal)

def checkBST(root):
    return _checkBST_(root, 0, 10000)
