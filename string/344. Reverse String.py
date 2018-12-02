class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]


class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        l1 = list(s)
        for i in range(len(s) // 2):
            l1[i], l1[len(s) - 1 - i] = l1[len(s) - 1 - i], l1[i]
        return ''.join(l1)
