class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        
        head = fast = ListNode(0)
        
        while l1 and l2:
            if l1.val < l2.val:
                fast.next= l1
                l1 = l1.next
            else: 
                fast.next = l2
                l2=l2.next
            
            fast = fast.next
        
        if not l1:
            fast.next = l2
        
        if not l2:
            fast.next = l1
            
        return head.next
            
            
