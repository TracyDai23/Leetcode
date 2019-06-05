# My success trial after watching explaination. 34.42%
# 逻辑大概想到了，但是多重function的recursion的调用和实现不是太明白
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        # self.cnt = 0
        t=0
        self.sum = sum
        if not root:
            return 0
        
        def dfs(root,t):
            cnt=0
            if not root:
                return 0
            
            t+=root.val
            # print('process:', root.val,t,cnt,self.sum)
            if t == self.sum:
                cnt+=1
                # print('append: ',root.val,t,cnt)
            # print(root.val,t)
            cnt+=dfs(root.left,t)
            cnt+=dfs(root.right,t)
            return cnt

        return dfs(root,0)+self.pathSum(root.left,sum)+self.pathSum(root.right,sum)

# My second trial: wrong answer
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.cnt = 0
        # self.sum = sum
        if not root:
            return 0
        
        def dfs(root,t):
            if not root:
                # t=0
                return 0
            
            t+=root.val
            if t == self.sum:
                self.cnt+=1
                print('append: ',root.val,t,self.cnt)
            print(root.val,t)
            dfs(root.left,t)
            dfs(root.right,t)

        dfs(root,0)
        # self.pathSum(root.left,0)
        # self.pathSum(root.right,0)
        return self.cnt 
            

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
            
