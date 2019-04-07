# Resolved 23.29%
# Checked discussion solutions. Similar concepts.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
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
                return True
        # print('d, c:', d, c)
        return False
