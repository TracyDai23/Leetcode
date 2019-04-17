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
    
# My Recursion solution: 61%
# Logic: inorder traversal,  fill in 'n' when null value present. Tedious corner cases.
# TC: O(N)
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        self.res =[]
        if not root: return True
        else:
            l= self.getVal(root)
        print(l)
        return l == l[::-1]
        
    def getVal(self,root):
        if root and root.left and root.right:
            self.getVal(root.left)
            self.res.append(root.val)
            self.getVal(root.right)
        elif root and (( not root.left and root.right) or (not root.right and root.left)):
            self.getVal(root.left)
            if not root.left: self.res.append('n')
            else:self.res.append(root.left.val)
            self.res.append(root.val)
            if not root.right: self.res.append('n')
            else:self.res.append(root.right.val)
            self.getVal(root.right)
        elif root:
            self.res.append(root.val)
        return self.res



# Other's recursion solution: 17% very clear and concise
class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True
        else:
            return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False

        if left.val == right.val:
            outPair = self.isMirror(left.left, right.right)
            inPiar = self.isMirror(left.right, right.left)
            return outPair and inPiar
        else:
            return False
