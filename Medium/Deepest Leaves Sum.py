# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def maxDepth(root):
            if not root: return 0
            return 1+max(maxDepth(root.left),maxDepth(root.right))
        
        def sameDepth(root,d):
            if not root:return 0
            if d==depth:
                self.ans+=root.val
                
            sameDepth(root.left,d+1)
            sameDepth(root.right,d+1)
            
        self.ans=0
        depth=maxDepth(root)
        sameDepth(root,1)
        return self.ans