# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or k == 0:
            return head
        t = head
        length = 1
        while t.next:
            length += 1
            t = t.next
        t.next = head

        t2 = head
        index = length - k % length
        i2 = 1
        while i2 < index:
            t2 = t2.next
            i2 += 1
        result = t2.next
        t2.next = None
        return result
