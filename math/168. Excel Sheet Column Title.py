class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        t = ''
        while n:
            t = chr(65 + (n - 1) % 26) + t
            n = (n - 1) // 26

        return t
