class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def trec(r, ma):
            return trec(r.left, max(ma, r.val)) + trec(r.right, max(ma, r.val)) + (r.val >= ma) if r else 0
        
        return trec(root, root.val)
