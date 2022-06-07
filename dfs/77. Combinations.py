class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.dfs([i for i in range(1, n + 1)], k, [], res)
        return res

    def dfs(self, nums, n, path, res):
        if n == 0:
            res.append(path)

        for idx, num in enumerate(nums):
            self.dfs(nums[idx + 1:], n - 1, path + [num], res)
