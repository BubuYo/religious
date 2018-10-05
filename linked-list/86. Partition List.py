# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        dummy1, dummy2 = ListNode(0), ListNode(0)
        j, k = dummy1, dummy2
        while head:
            if head.val < x:
                j.next = head
                j = head
            else:
                k.next = head
                k = head
            head = head.next
        k.next = None
        j.next = dummy2.next
        return dummy1.next
