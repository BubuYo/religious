class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, path, res):
        res.append(path)

        if len(nums) == 0:
            return

        for idx, num in enumerate(nums):
            self.dfs(nums[idx + 1:], path + [num], res)
