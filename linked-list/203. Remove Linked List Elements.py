# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return
        while head and head.val == val:
            head = head.next
        ans = head
        while head and head.next:
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next
        return ans
