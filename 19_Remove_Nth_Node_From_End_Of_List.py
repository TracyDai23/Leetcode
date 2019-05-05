# Linked List: 92.84%
# Time complexity: O(N)
# Another solution is one pass with two pointers always keep distance as n

# two pass solution
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # get linked list size
        s= 1
        dummy=c=head
        if n ==0:
            return None
        while head.next:
            s+=1
            head = head.next
        # return s
        k = s-n
        # print(c, k)
        if k == 0:
            dummy=c.next
        else:
            while k-1 and k!= 0:
                c=c.next
                k-=1
                # print(c.val)
            c.next= c.next.next
        return dummy

# One pass solution:
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # get linked list size
        s= 1
        slow=fast=head
        if n ==0:
            return None
        for i in range(n):
            fast = fast.next
            # print(slow.val, fast.val)
        if not fast:
            head = head.next
        else:
            while fast.next:
                # print(slow.val, fast.val)
                fast=fast.next
                slow = slow.next
            slow.next = slow.next.next
        return head
