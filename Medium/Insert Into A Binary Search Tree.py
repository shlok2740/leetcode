# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        original_root=root
        
        while root:
            if val<root.val:
                if not root.left:
                    root.left=TreeNode(val)
                    break
                root=root.left
            
            elif val>root.val:
                if not root.right:
                    root.right=TreeNode(val)
                    break
                root=root.right
        
        
        return original_root