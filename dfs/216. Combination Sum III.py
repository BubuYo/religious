class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        self.dfs(range(1, 10), k, n, [], res)
        return res

    def dfs(self, nums, k, n, path, res):
        if n < 0:
            return

        if k == 0 and n == 0:
            res.append(path)

        for idx, num in enumerate(nums):
            self.dfs(nums[idx+1:], k - 1, n - num, path + [num], res)
