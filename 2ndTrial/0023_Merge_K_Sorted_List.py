# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from heapq import *
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []
        counter = 0
        for l in lists:
            head = ListNode(0)
            
            while l:
                head = l
                counter+=1
                print(head.val, counter)
                heappush(heap, (head.val, counter, head))
                l = l.next
        # print([item[0] for item in heap])
        dummy = head = ListNode(0)
        while heap:
            head.next = heappop(heap)[2]
            head = head.next
        return dummy.next
            
