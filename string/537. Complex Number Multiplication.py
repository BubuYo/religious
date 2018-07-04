class Solution:
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        ia, ib = a.index('+'), b.index('+')
        ai, aj = int(a[:ia]), int(a[ia + 1:-1])
        bi, bj = int(b[:ib]), int(b[ib + 1:-1])
        return '{}+{}i'.format(ai * bi - aj * bj, ai * bj + aj * bi)
