class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums, index, path, res):
            res.append(path)
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                dfs(nums, i + 1, path + [nums[i]], res)

        res = []
        dfs(sorted(nums), 0, [], res)
        return res
