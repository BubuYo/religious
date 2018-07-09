class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if not all([A, B]) or len(A) != len(B):
            return False
        if A == B:
            return len(set(A)) != len(A)
        count = 0
        j, k = '', ''
        d = {ia: a for ia, a in enumerate(A)}
        for ib, b in enumerate(B):
            if d[ib] != b:
                j += d[ib]
                k += b
                count += 1
        return count == 2 and j == k[::-1]
