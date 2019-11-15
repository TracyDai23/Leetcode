class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        # edge case:
        if not t:
            return True
        def check(s, t):
            if not s:
                return False
            if s.val == t.val and dfs(s, t):
                return True
            return check(s.left, t) or check(s.right, t)
            
        def dfs(s, t):
            if not s and not t:
                return True
            if (not s and t) or (not t and s):
                return False
            
            if s.val == t.val and dfs(s.left, t.left) and dfs(s.right, t.right):
                return True
        
        return check(s,t)
