class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        tmp = ['[]', '{}', '()']
        for i in s:
            stack.append(i)
            if len(stack) > 1 and stack[-2] + stack[-1] in tmp:
                stack.pop()
                stack.pop()
        return not stack
