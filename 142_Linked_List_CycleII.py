# Resolved 20%


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        d={}
        c=head
        while c:
            try:
                d.pop(c)
            except:
                d[c] = 1
                c= c.next
            else:
                return c

        return None
