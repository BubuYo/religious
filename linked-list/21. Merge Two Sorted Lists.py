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
        p = dummy = ListNode('bububububu')
        while l1 and l2:
            p.next = ListNode(min(l1.val, l2.val))
            if l1.val < l2.val:
                l1 = l1.next
            else:
                l2 = l2.next
            p = p.next
        p.next = l1 if l1 else l2
        return dummy.next
