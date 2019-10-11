# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def merge(self,h1, h2):
        dummy = tail = ListNode(None)
        while h1 and h2:
            if h1.val<h2.val:
                tail.next, tail, h1 = h1,h1,h1.next
            else:
                tail.next, tail, h2 = h2, h2, h2.next
        
        tail.next = h1 or h2 # the while portion only consider when both h1 and h2 has elements. WHen one list exhausted, still want to link the left element back to the tail. This is the function of this line
        return dummy.next
    
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pre,slow,fast = None, head, head
        while fast and fast.next:
            pre,slow,fast = slow, slow.next, fast.next.next
        pre.next = None
        
        return self.merge(*map(self.sortList,(head,slow))) # equals to self.merge(self.sortList(head), self.sortList(slow))
