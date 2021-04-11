# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def trec(r, ma):
            return trec(r.left, max(ma, r.val)) + trec(r.right, max(ma, r.val)) + (r.val >= ma) if r else 0
        
        return trec(root, root.val)
            
                
            
