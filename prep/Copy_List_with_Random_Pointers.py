class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        dic = dict()
        m = n = head
        while m:
            dic[m] = Node(m.val,None,None)
            m = m.next
        while n:
            dic[n].next = dic.get(n.next)
            # print('n, dic[n], dic.get(n.next)', n,dic[n], dic.get(n.next))
            dic[n].random = dic.get(n.random)
            n = n.next
        return dic.get(head)

    
# Xudong Solution
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dic = {}
        res = curr = Node(0,None,None)
        curr.next = head
       
        while head:
           
            if head:
                if head not in dic:
                    dic[head] = Node(head.val,None,None)
                curr.next = dic[head]

            if head.random:
                if head.random not in dic:
                    dic[head.random] = Node(head.random.val,None,None)
                curr.next.random = dic[head.random]
               
            head = head.next
            curr = curr.next            

               
        return res.next
