class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        start = 0
        for item in s:
            position = t[start:].find(item)
            if position == -1:
                return False
            start += position + 1
        return True
