class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        if len(strs) == 1:
            return strs[0]
        if not all(strs):
            return ''
        ans = ''
        index = 0
        for i in strs[0]:
            for s in strs:
                if not s[index:].startswith(i):
                    return ans
            else:
                ans += i
            index += 1
        return ans
