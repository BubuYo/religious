class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists: return
        def merge(l1, l2):
            t = dummy = ListNode('bububububu')
            while l1 and l2:
                if l1.val < l2.val:
                    t.next = l1
                    l1 = l1.next
                else:
                    t.next = l2
                    l2 = l2.next
                t = t.next
            t.next = l1 if l1 else l2
            return dummy.next

        i = 1
        k = len(lists)
        while i < k:
            for j in range(0, k - i, i * 2):
                lists[j] = merge(lists[j], lists[i + j])
            i *= 2
        return lists[0]


