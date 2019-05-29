# C: May 28th
class Solution:
    # def __init__(self):
        # self.k = 0
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k=k
        self.res = 0
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            self.k-=1
            if self.k == 0:
                self.res= root.val

            dfs(root.right)
        
        dfs(root)
        return self.res
        

# Other's solution: python generator
def iterate_tree(root):
    # inorder tree traversal generator
    if root.left:
        for i in iterate_tree(root.left):
            yield i
    yield root
    if root.right:
        for i in iterate_tree(root.right):
            yield i

class Solution(object):
    def kthSmallest(self, root, k):
        # iterate over tree
        for p, v in enumerate(iterate_tree(root)):
            if p+1 == k:
                return v.val
