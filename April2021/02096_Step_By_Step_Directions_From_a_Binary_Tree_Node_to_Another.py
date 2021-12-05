# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        self.p = []
        
        def rootDown(root,v,path,found):
            # print('start', v, self.p)
            if not root or found:
                return
            if root.val == v:
                found=True
                self.p = path.copy()
                # print('bingo', self.p)
                return path
            if root.left:
                # print('hit left')
                rootDown(root.left,v,path+['L'],found)
            if root.right:
                rootDown(root.right,v,path+['R'],found)
        
        
        rootDown(root,startValue,[],False)
        s_path=self.p
        self.p = []
        rootDown(root,destValue,[],False)
        d_path= self.p
        # print('final',s_path, d_path)

        while s_path and d_path:
            s = s_path.pop(0)
            d = d_path.pop(0)
            if s !=d:
                return 'U'*(len(s_path) + 1) + d + ''.join(d_path)
            
        if not s_path:
            return ''.join(d_path)
        if not d_path:
            return 'U'*(len(s_path))
