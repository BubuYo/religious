class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.dfs(candidates, target, [], res)
        return res

    def dfs(self, nums, n, path, res):
        '''

        :param nums: 候选数字 list
        :param n: 还差多少
        :param path: 当前可能成功的 list
        :param res:
        :return:
        '''
        if n < 0:
            return  # 超了
        if n == 0:
            res.append(path)  # 够了
        for idx, num in enumerate(nums):
            self.dfs(nums[idx:], n - num, path + [num], res)
