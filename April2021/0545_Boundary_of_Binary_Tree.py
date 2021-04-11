# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        res = []
        llist = []
        leaf = []
        rlist = []

        if not root:
            return []
        else:
            res.append(root)
        
        #corner case: [1]
        if not root.left and not root.right:
            return [root.val]
        
        def trec(root):
            if not root:
                return
            
            # print("current root val: ", root.val)
            #leaf portion
            if not (root.left or root.right):
                leaf.append(root)
                # print("llist: ",llist, "leaf: ", leaf, "rlist: ", rlist)
                return
            
            # left boundary portion:
            if (root in llist or root in res) and root.left and (root.left.left or root.left.right):
                llist.append(root.left)
            elif (root in llist) and root.right and not root.left and (root.right.left or root.right.right):
                llist.append(root.right)
            
            # right boundary portion
            if (root in rlist or root in res) and root.right and (root.right.left or root.right.right):
                rlist.append(root.right)
            elif (root in rlist) and root.left and not root.right and (root.left.left or root.left.right):
                rlist.append(root.left)
                
            # print("llist: ",llist, "leaf: ", leaf, "rlist: ", rlist)
            
            trec(root.left)
            trec(root.right)
            
            
        trec(root)
        result =[]
        for r in res+llist+leaf+rlist[::-1]:
            result.append(r.val)
    
        
        return result
        
        
        
