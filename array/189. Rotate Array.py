class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        while k >= N:
            k -= N
        if k != 0:
            nums[:] = nums[-k:] + nums[:N - k]
