# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def ino(root):
            return ino(root.left)+[root.val]+ino(root.right) if root else []
        
        return ino(root)[k-1]