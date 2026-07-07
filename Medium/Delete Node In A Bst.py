class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return
        if root.val>key:
            root.left = self.deleteNode(root.left,key)
        
        elif root.val<key:
            root.right = self.deleteNode(root.right,key)
        
        elif root.val==key:
            
            if root.left and root.right:
                min_node = self.min_node(root.right)
                root.val, min_node.val = min_node.val, root.val
                root.right = self.deleteNode(root.right,key)
            
            elif root.left or root.right:
                return root.left if root.left else root.right
            else:
                return None
        
        return root
    
    def min_node(self,root):
        
        while root.left:
            root = root.left
        
        return root