# My first trial: 基本是对的，唯一的bug是line 22 的return将结束后续左孩子和右孩子的执行。所以去掉line22就好。
#95.8%
# 本题的base case是当res的长度等于当前floor level（k） 的时候就append。因此实现了有右孩子加右孩子，没有右孩子加最右的左孩子的需求。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        self.res=[]
        # self.level =0
        def dfs(root,k):
            
            if not root:
                return None
            #base case:
            if k == len(self.res):
                self.res.append(root.val)
                #return # 错误在此处不能return，因为return将直接结束当前recursion而不再执行后面的dfs(root.right, k+1) 和dfs(root.left, k+1)了。
            dfs(root.right,k+1)
            dfs(root.left,k+1)
        dfs(root,0)
