class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        ans = '1'
        for _ in range(n - 1):
            char, count, tmp = ans[0], 0, ''
            for i in ans:
                if char == i:
                    count += 1
                else:
                    tmp, char, count = tmp + str(count) + char, i, 1
            tmp += str(count) + char
            ans = tmp
        return ans
