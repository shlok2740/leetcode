# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root, min_value=-10000):
        return self.goodNodes(root.left, max(min_value, root.val)) + self.goodNodes(root.right, max(min_value, root.val)) + (root.val >= min_value) if root else 0