# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(node,parent,grandparent):
            if not node:
                return None
            
            if parent and grandparent and grandparent.val%2==0:
                self.ans+=node.val
                
            dfs(node.left,node,parent)
            dfs(node.right,node,parent)
            
        self.ans=0
        dfs(root,None,None)
        return self.ans