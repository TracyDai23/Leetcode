# In short, in this recursion question, I was stuck on the sub-function and global varialbe. This is a great example not to use global variable.

# My third tiral with reference to other's solutions:
# 73.01%, improved time by always pop out the first element from preorder. 
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
            
            
        if not inorder or not preorder:
            return None
        t=TreeNode(preorder[0])
        root_spliter = inorder.index(preorder.pop(0))

        left_in = inorder[:root_spliter]
        # left_pre = preorder[1:len(left_in)+1]
        t.left = self.buildTree(preorder,left_in)

        right_in = inorder[root_spliter+1:]
        # right_pre = preorder[-len(right_in):]
        t.right=self.buildTree(preorder,right_in)

        return t

# My second trial: succeed 21.00% 
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
            
            
        if not preorder or not inorder:
            return None
        t=TreeNode(preorder[0])

        left_in = inorder[:inorder.index(t.val)]
        left_pre = preorder[1:len(left_in)+1]
        t.left = self.buildTree(left_pre,left_in)

        right_in = inorder[inorder.index(t.val)+1:]
        right_pre = preorder[-len(right_in):]
        t.right=self.buildTree(right_pre,right_in)

        return t



# My first trial: did not figure out the solution
# Issue: stuck on sub-function rec and global variable. Since this recursion question need exactly the same variable as orignal function,
#         and just need to return one result, there is no need to create a global variable to complicate it. 
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.t=TreeNode(0)
        print('initial self.t: ',self.t)
        def rec(preorder, inorder,t=self.t):
            
            
            if not preorder or not inorder:
                return
            
            rootval = preorder[0]
            print('new round: ',rootval,preorder,inorder)
            # print('left_in,left_pre,right_in,right_pre: ',left_in,left_pre,right_in,right_pre)
        
            t.val = rootval
            print('t,self.t: ',t,self.t)
            # if left_in:
            t.left=TreeNode(0)
            left_in = inorder[:inorder.index(rootval)]
            left_pre = preorder[1:len(left_in)+1]
            rec(left_pre,left_in,t.left)
            # if right_in:
            t.right = TreeNode(0)
            right_in = inorder[inorder.index(rootval)+1:]
            right_pre = preorder[-len(right_in):]
            t.right=rec(right_pre,right_in,t.right)
            
        rec(preorder,inorder)
        return self.t
            
