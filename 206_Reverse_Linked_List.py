# Wrong answer attempt on 10/15/2019
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # dummy = ListNode(0)
        rsv= tail = head
        while head.next.next:
            tail = head.next
            rsv = tail.next
            tail.next = head
            head.next = rsv
            # print(head.val, tail.val)
            # finished first reverse and move to next
            # head, tail = tail.next, head
            # print(head.val, tail.val)
        return head
