# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        stk = [[root]]
        level = 1
        res = []           
        #BFS starts
        while stk:
            #get all rootnotes at the same level
            tmp = stk.pop(0)
            l = []
            for rt in tmp: #loop roots at the same level
                if rt:
                    l.append(rt.val)
            # append to result in zigzag order
            if level%2 ==0: 
                res.append(l[::-1])
            else:
                res.append(l)
            
            l = []
            for i in range(len(tmp)):
                if not tmp[i]:
                    continue
                if tmp[i].left:
                    l.append(tmp[i].left)
                if tmp[i].right:
                    l.append(tmp[i].right)
            if l != []:
                stk.append(l)
            level+=1
        return res
            
                
            
        
