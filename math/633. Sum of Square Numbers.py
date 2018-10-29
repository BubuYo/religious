class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        l, r = 0, int(c ** 0.5)
        while l <= r:
            t = l ** 2 + r ** 2
            if t > c:
                r -= 1
            elif t < c:
                l += 1
            else:
                return True
        return False
