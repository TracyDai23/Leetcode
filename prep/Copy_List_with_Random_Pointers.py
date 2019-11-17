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
