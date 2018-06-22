class Solution:
    def makeLargestSpecial(self, S):
        """
        :type S: str
        :rtype: str
        """
        subs, tmp, count = [], 0, 0
        for i, j in enumerate(S):
            count = count + 1 if j == '1' else count - 1
            if count == 0:
                res = self.makeLargestSpecial(S[tmp+1: i])
                subs.append(''.join(['1', res, '0']))
                tmp = i + 1
        return ''.join(sorted(subs, reverse=True))
