# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def dfs(root,previous):
            if not root :
                return
            
            current=previous+root.val
            
            x=current-targetSum
            
            if x in freq:
                self.count+=freq[x]
            
            if current in freq:
                freq[current]+=1
            
            else:
                freq[current]=1
                
            dfs(root.left,current)
            dfs(root.right,current)
            freq[current]-=1
        
        self.count=0
        freq={0:1}
        dfs(root,0)
        return self.count