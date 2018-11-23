class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """

        ans, i = 0, 5
        while i <= n:
            ans += n // i
            i *= 5
        return ans
