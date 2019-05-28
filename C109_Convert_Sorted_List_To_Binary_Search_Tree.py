# read answer
# BTS, 重点是BTS的构建， 难点是linked list怎么用two pointer approach找mid point

class Solution:
    def findMiddle(self, head):

        # The pointer used to disconnect the left half from the mid node.
        prevPtr = None
        slowPtr = head
        fastPtr = head

        # Iterate until fastPr doesn't reach the end of the linked list.
        while fastPtr and fastPtr.next:
            prevPtr = slowPtr #存住slowptr的上一个节点位置，这样可以用于最后的linked list分开
            slowPtr = slowPtr.next # 每次跳一格
            fastPtr = fastPtr.next.next # 每次跳两格，用于使slowptr 找到中点

        # Handling the case when slowPtr was equal to head.
        
        if prevPtr:
            prevPtr.next = None # 断开左子树的部分。通过让中点前的最后一个linked list element的next 为none。

        return slowPtr


    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        # If the head doesn't exist, then the linked list is empty
        if not head:
            return None

        # Find the middle element for the list.
        mid = self.findMiddle(head)

        # The mid becomes the root of the BST.
        node = TreeNode(mid.val)

        # Base case when there is just one element in the linked list
        if head == mid:
            return node

        # Recursively form balanced BSTs using the left and right halves of the original list.
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)
        return node
        
