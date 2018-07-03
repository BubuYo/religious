class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        t = {}
        for i in s:
            if i in t:
                t[i] += 1
            else:
                t[i] = 1
        m = float('inf')
        ans = -1
        for k, v in t.items():
            tmp = s.index(k)
            if v == 1:
                if tmp < m:
                    ans = tmp
                m = min(tmp, m)

        return ans
