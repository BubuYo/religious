# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p = dummy = ListNode(-1)
        while l1 or l2:
            tmp1 = l1.val if l1 else float('inf')
            tmp2 = l2.val if l2 else float('inf')
            p.next = ListNode(min(tmp1, tmp2))
            if tmp1 < tmp2:
                l1 = l1 and l1.next
            else:
                l2 = l2 and l2.next
            p = p.next
        return dummy.next
