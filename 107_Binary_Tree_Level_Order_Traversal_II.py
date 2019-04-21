# Other's solution
# bfs + queue
# first bfs question. 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    # bfs + queue   
    def levelOrderBottom(self, root):
        queue, res = collections.deque([(root, 0)]), []
        while queue:
            node, level = queue.popleft() # not quite sure why it needs to popleft(). 04212019
            if node:
                if len(res) < level+1:
                    res.insert(0, [])
                res[-(level+1)].append(node.val)
                queue.append((node.left, level+1))
                queue.append((node.right, level+1))
                print(queue, res)
        return res
