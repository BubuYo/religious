class Solution:
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        F5, half = {str(10 ** len(n) + 1), str(10 ** (len(n) - 1) - 1)}, int(n[:(len(n) + 1) // 2])
        for h in map(str, [half - 1, half, half + 1]):
            F5.add(h + [h, h[:-1]][len(n) & 1][::-1])
        return min([(abs(int(i) - int(n)), int(i), i) for i in F5 if i != n])[-1]
