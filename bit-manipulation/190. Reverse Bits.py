class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        b = bin(n)[2:]
        if len(b) < 32:
            b = '0' * (32 - len(b)) + b
        return int("0b" + b[::-1], 2)
