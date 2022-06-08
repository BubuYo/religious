class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        self.dfs(range(1, 10), k, n, 0, [], res)
        return res

    def dfs(self, nums, k, n, index, path, res):
        if k < 0 or n < 0:
            return

        if k == 0 and n == 0:
            res.append(path)

        for idx, num in enumerate(nums):
            if idx < index:
                continue
            self.dfs(nums, k - 1, n - num, idx + 1, path + [num], res)
