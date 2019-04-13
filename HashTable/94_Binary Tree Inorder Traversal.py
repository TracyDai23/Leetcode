#94 Binary Tree Inorder Traversal  
''' 
    先序遍历 (preorder)：先根、后左、再右
    中序遍历 (inorder)：先左、后根、再右
    后序遍历 (postorder)：先左、后右、再根
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        # def moveUp(root):
        #     if self.left and self.right: 
        #         return [self.val]
        #     elif self.left and not self.right:
        #         return [self.val, self.]
        res = []
        self.helper(root,res)
        return res
    
    def helper(self,root,res):
        if root:
            self.helper(root.left,res)
            res.append(root.val)
            self.helper(root.right,res)

  # Iterate solution: 
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        solution = []
        node = root
        while node or len(stack)>0:
            if node!= None:
                stack.append(node) #In this step, stack stores node object, not node value
                node = node.left
            else: 
                node = stack.pop()
                solution.append(node.val)
                node = node.right
        return solution
