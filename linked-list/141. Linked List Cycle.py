# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        while fast and slow:
            fast = fast.next
            if fast is slow:
                return True
            if fast:
                fast = fast.next
            slow = slow.next
        return False
