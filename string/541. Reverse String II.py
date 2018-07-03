class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        L = len(s)
        if L < k:
            return s[::-1]
        elif L < 2 * k:
            return s[:k][::-1] + s[k:]
        else:
            return s[:k][::-1] + s[k:k * 2] + self.reverseStr(s[2 * k:], k)
