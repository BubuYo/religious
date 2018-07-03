class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub(r'\W+', '', s).lower()
        # 题目里说了只考虑字母，我就把数字过滤掉了，然而不能 AC， 很迷
        # s = ''.join([i for i in s if i not in '0123456789'])
        L = len(s)
        return s[:L // 2] == s[(L + 1) // 2:][::-1]
