class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums)
        while l < r:
            t = (l + r) // 2
            if nums[t] > nums[r]:
                l = t + 1
            elif nums[t] < nums[r]:
                r = t
            else:
                r -= 1
        return nums[l]
