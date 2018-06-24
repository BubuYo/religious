class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        t = [0, 0] + [1 for i in range(n - 2)]
        for i in range(2, int(math.sqrt(n)) + 1):
            if t[i]:
                for j in range(i * i, n, i):
                    t[j] = 0
        return sum(t)
