class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        b = bin(n)[2:]
        if len(b) < 32:
            b = '0' * (32 - len(b)) + b
        return int("0b" + b[::-1], 2)


class Solution:
    def reverseBits(self, n):
        ans = 0
        for _ in range(32):
            ans = (ans << 1) | (n & 1)
            n >>= 1
        return ans


class Solution:
    def reverseBits(self, n: int) -> int:
        return int(bin(n).split("0b")[-1].zfill(32)[::-1], 2)
