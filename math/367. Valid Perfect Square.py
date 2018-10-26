class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l, r = 0, num
        while l <= r:
            mid = (l + r) // 2
            t = mid * mid
            if t < num:
                l = mid + 1
            elif t > num:
                r = mid - 1
            else:
                return True
        return False
