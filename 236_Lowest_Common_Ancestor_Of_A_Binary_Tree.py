# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = root.val
        self.p= []
        def dfs(root,p=p,q=q):
            if not root:
                return 0
            dfs(root.left)
            dfs(root.right)
            
            if root.val == p or root.val==q:
                p.append(root.val)
            if root.left.val in p and root.right.val in p:
                self.res= root.val
            elif root.left.val == p[0] or root.right.val == p[0]:
                self.p[0] = root.val
            elif root.left.val == p[1] or root.right.val == p[1]:
                self.p[1] = root.val
                
        
        dfs(root)
        return self.res
        
    
