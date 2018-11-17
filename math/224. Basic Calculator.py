class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        num, sign, result = 0, 1, 0
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '+':
                result += sign * num
                sign, num = 1, 0
            elif c == '-':
                result += sign * num
                sign, num = -1, 0
            elif c == '(':
                stack += [result]
                stack += [sign]
                result, sign = 0, 1
            elif c == ')':
                result += sign * num
                result *= stack.pop()
                result += stack.pop()
                num = 0
        result += sign * num
        return result
