class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = []
        height = 0
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            height += 1
            root = root.right
        return (height)