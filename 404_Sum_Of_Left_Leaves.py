# 84.84%

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.res = 0
        
        def dfs(root):
            if not root:
                return 0
            dfs(root.left)
            dfs(root.right) 
            # base case
            if root.left and not root.left.left and not root.left.right:
                self.res+=root.left.val
            
        dfs(root)
        return self.res
