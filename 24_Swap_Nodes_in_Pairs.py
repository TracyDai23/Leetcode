# Resolved 80.95%
# Corner case: need to consider if linked list does not have even nodes. Corrected at line 23. 

# Recursive solution listed after the Iterative solution.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head
        
        current = head
        print(current)
        dummy = head.next
        print(dummy)
        slow = current
        fast = current.next
        while current and current.next:
            slow.next = current.next
            slow = current
            fast = current.next
            #print('slow, fast: ', slow.val, fast.val)
            current.next = fast.next # move current fast location
            fast.next = slow 
            #print('fast.next.val after swapping:', fast.next.val)
            slow.next = current.next
            #print('slow.next.val after swapping:', slow.next.val)
            current = slow.next
            #print('current val:',current.val)
            
        return dummy

    
# Recursion Method after reading other's discussion

class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next: return head
        new_start = head.next.next
        head, head.next = head.next, head
        head.next.next = self.swapPairs(new_start)
        return head
        
