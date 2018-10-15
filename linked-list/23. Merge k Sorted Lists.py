class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return

        def merge(l1, l2):
            dummy = ListNode('bububububu')
            t = dummy
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
        ans = lists[0]
        for i in range(1, k):
            ans = self.mergeTwoLists(mergedList, lists[i])
        return ans

        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = merge(lists[i], lists[i + interval])
            interval *= 2
        return lists[0]


# Python3.5 中，heapq 的比较函数从 __cmp__ 变成了 __lt__,
# 导致下面的代码在 Python 2 里可以正常允许，3 里面会报错
# TypeError: unorderable types: ListNode() < ListNode()

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        for i in lists:
            if i:
                heap.append((i.val, i))
        heapq.heapify(heap)
        t = dummy = ListNode(0)
        while heap:
            i = heapq.heappop(heap)[1]
            t.next = i
            t = t.next
            if i.next:
                heapq.heappush(heap, (i.next.val, i.next))
        return dummy.next
