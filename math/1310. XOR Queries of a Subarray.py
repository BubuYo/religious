class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xors = [0 for _ in range(len(arr) + 1)]
        for idx, i in enumerate(arr):
            xors[idx + 1] = xors[idx] ^ i
        ans = []
        for lr in queries:
            l, r = lr
            ans.append(xors[r + 1] ^ xors[l])
        return ans

