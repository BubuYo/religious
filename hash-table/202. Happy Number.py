class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        occured = set()
        while n != 1:
            total = 0
            for s in str(n):
                total += int(s)**2
            if total in occured:
                return False
            occured.add(total)
            n = total
        return True
