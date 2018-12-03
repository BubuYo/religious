class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        v = 'aeiouAEIOU'
        s = list(s)
        l, r = 0, len(s) - 1
        while l < r:
            while s[l] not in v and l < r:
                l += 1
            while s[r] not in v and l < r:
                r -= 1
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return ''.join(s)


class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        tmp, indexs = list(s), [idx for idx, i in enumerate(s) if i in 'aeiouAEIOU']
        for i in range(len(indexs) // 2):
            tmp[indexs[i]], tmp[indexs[-i - 1]] = tmp[indexs[-i - 1]], tmp[indexs[i]]
        return ''.join(tmp)
