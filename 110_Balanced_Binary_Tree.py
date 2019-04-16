# Other's solution
# recursion method, defined a self.flag variable that has been used and updated in another function getHeight(root) with no need to return.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.flag = True
        self.getHeight(root)
        return self.flag
        
        
    def getHeight(self, root):
        if not root: return 0
        
        lh = self.getHeight(root.left)
        rh = self.getHeight(root.right)
        
        if abs(lh-rh)>1:
            self.flag = False
        
        return max(lh,rh)+1
