class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.res = None
        # self.cur = root
        def dfs(r):     
            if not r:
                return None
                      
            dfs(r.right)
            dfs(r.left)
             
            r.right = self.res
            r.left = None
            self.res= r
            return
        
        dfs(root)


# My first trial: 
# 1） 这个答案里res的最初设置可以直接设置成none； 
# 2） dfs() 的recursion引用应该是dfs(r.right) dfs(r.left) 然后再是关于root的操作。这个顺序是根据遍历的方式来的。
#       preorder traversal:  root的操作，dfs(root.left), dfs(root.right)
#       inorder traversal: dfs(root.left), root的操作，dfs(root.right)
#       postorder traversal: dfs(root.left), dfs(root.right), root的操作
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.res = root
        self.cur = root
        def dfs(r):
            
            if not r:
                return None
            
            
            dfs(r.right)
            r.right = self.res
            r.left = None
            self.res.val = r.val
            dfs(r.left)
        
        dfs(root)
        return self.res
