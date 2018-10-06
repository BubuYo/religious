# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        map = {}
        while head:
            if head in map:
                return head
            else:
                map[head] = 'bigdog695'
            head = head.next
        return
