# Iterataion solution: 99%
# Logic: 1) pull tree node value at the same level into a list, and then compare the list between straight order and reverse order. 
#         2)fill 'n'(special character) to fill in list position; 3) add flag to stop move down when reach the bottom of the tree
# Time complexity: Nlog(N), Log(N) is the "While" loop to jump between tree layers, N is the "for" loop portion.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        l= []
        pl=[root]
        h=[]
        m = True # flag to move to next level of tree

        while pl and m:
            m=False
            for i in range(len(pl)):
                # how to handle parent.child node is None case?
                # In this problem, I filled a special character to mark position.
                if not pl[i].left:
                    l.append('n')
                else:
                    l.append(pl[i].left.val)
                    m=True
                    h.append(pl[i].left)
                if not pl[i].right:
                    l.append('n')
                else:
                    l.append(pl[i].right.val)
                    m=True
                    h.append(pl[i].right)
            if l!= l[::-1]:
                return False
            else:
                pl=h
                h=[]
                l=[]
        return True
