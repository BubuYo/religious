class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [0] + nums
        for i in range(3, len(nums)):
            nums[i] = max(nums[i] + nums[i - 2], nums[i] + nums[i - 3])
        return max(nums)

# OR


class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        l, r = 0, nums[0]
        for i in range(1, len(nums)):
            l, r = max(l, r), l + nums[i]
        return max(l, r)
