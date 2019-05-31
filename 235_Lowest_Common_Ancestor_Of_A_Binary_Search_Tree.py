# My own solution: 97.78%
# Recursion: preorder.
#Time complexity: O(N)where NN is the number of nodes in the BST. In the worst case we might be visiting all the nodes of the BST.
#??Space complexity: O(N). This is because the maximum amount of space utilized by the recursion stack would be NN since the height of a skewed BST could be NN. 
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = None
        def dfs(root, p,q):
            if not root:
                return
            if root.val >=p.val and root.val <=q.val:
                self.res = root
                # print(self.res)
            elif root.val > p.val and root.val > q.val:
                dfs(root.left,p,q)
            elif root.val<p.val and root.val <q.val:
                dfs(root.right,p,q)
        
        if p.val >q.val:
            p,q = q,p
        dfs(root,p,q)
        return self.res
