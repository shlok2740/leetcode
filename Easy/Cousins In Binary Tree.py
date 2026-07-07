# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        foundNodes=[]
        
        def search(root,parent,depth):
            if not root:
                return 
            
            if root.val==x or root.val==y:
                foundNodes.append((parent,depth))
                
            search(root.left,root,depth+1)
            search(root.right,root,depth+1)
            
        search(root,None,0)
        return foundNodes[0][0]!=foundNodes[1][0] and foundNodes[0][1]==foundNodes[1][1]