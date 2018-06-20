# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        l, p = [], head
        while p is not None:
            l.append(p.val)
            p = p.next
        L = len(l)
        if L % 2:
            return l[:L // 2] == l[:L // 2:-1]
        return l[:L // 2] == l[:L // 2 - 1:-1]
