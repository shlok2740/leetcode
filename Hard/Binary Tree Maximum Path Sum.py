# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def maxPath(node):
            if not node:
                return 0
            left=maxPath(node.left)
            right=maxPath(node.right)
            self.max=max(self.max,left+node.val+right)
            return max(max(left,right)+node.val,0)
        self.max=-float('inf')
        maxPath(root)
        return self.max