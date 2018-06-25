class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = len(nums)
        for i in range(1, L):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)


# OR


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = csum = nums[0]
        for num in nums[1:]:
            if num >= csum + num:
                csum = num
            else:
                csum += num

            if csum > max_sum:
                max_sum = csum

        return max_sum
