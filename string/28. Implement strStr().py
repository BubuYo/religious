class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        for index, h in enumerate(haystack):
            if h == needle[0]:
                if haystack[index + 1:].startswith(needle[1:]):
                    return index
        return -1
