# Self-resolved! 98% 
# Resolved after CC189 LinkedList chapter.
''' Take-away: 1) create a dummynode to hold linked list. 
                2) if two linked lists are not equal size, need to consider add ListNode(0)
                3) need to consider place holder when d >0 LIne 32-33
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        c=s = ListNode(0)
        # print(s.val)
        d = 0
        while l1 or l2: 
            if l2 and not l1:
                l1= ListNode(0)
            
            elif l1 and not l2:
                l2 = ListNode(0)
            n = l1.val + l2.val
            s.val = (n+d)%10
            d = (n+d)//10            
            l1=l1.next
            l2=l2.next  
            if l1 or l2:
                s.next = ListNode(0)
                s=s.next
        if d >0:
            s.next = ListNode(d)
        return c
        
