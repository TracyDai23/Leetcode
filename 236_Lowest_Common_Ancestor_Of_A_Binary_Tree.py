# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# My third trial after go through other's result: wrong answer
# 错误原因是 line 41 没有写return dfs(root,p,q)， 而只写了dfs(root, p,q),所以没有输出任何东西。

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #step1: find p and q;
        #step2: source back to find common ancestor
        self.res = root
        # self.left = None
        # self.right = None
        def dfs(root,p,q):
            if not root:
                return None
            
            # base case:
            if root.val == p.val or root.val == q.val:
                return root
            
            # Major logic solution along with Check condition !!
            left = dfs(root.left,p,q)
            right = dfs(root.right,p,q)
            # print(self.left, self.right, self.res)
            # Check condition
            if left and right:
                return root
            elif not right:
                return left
            elif not left:
                return right

                
        
        return dfs(root,p,q)

        
    

# My second trial:
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #step1: find p and q;
        #step2: source back to find common ancestor
        self.res = None
        self.p1,self.p2 =None,None
        def dfs(root,p,q):
            if not root.left and not root.right:
                return 0
            dfs(root.left,p,q)
            dfs(root.right,p,q)
            
            if root.left.val == p.val or root.right.val==p.val or root.val == p.val:
                
            if root.
            if self.p1 or self.p2:
                print(self.p1,self.p2)
                return
#             if p1==root.val 
                
#             if root.left.val in p and root.right.val in p:
#                 self.res= root.val
#             elif root.left.val == p[0] or root.right.val == p[0]:
#                 self.p[0] = root.val
#             elif root.left.val == p[1] or root.right.val == p[1]:
#                 self.p[1] = root.val
                
        
        dfs(root,p,q)
        # return self.res
        

# My first trial:
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
        
    
