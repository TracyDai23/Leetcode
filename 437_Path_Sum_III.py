# My first trial: wrong answer
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.cnt = 0
        self.sum = sum
        def dfs(root,t):
            if not root:
                return 0
            
            if t == self.sum:
                self.cnt+=1
                print('append: ',root.val,t,self.cnt)
                return
            else:
                print(root.val,t)
                t+=root.val
                dfs(root.left,t)
                dfs(root.right,t)
            print('new round')
            dfs(root.left,t=0)
            dfs(root.right,t=0)
        
        dfs(root,0)
        return self.cnt 
            
