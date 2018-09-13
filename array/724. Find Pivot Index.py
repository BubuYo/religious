class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count, total = 0, sum(nums)
        for i, n in enumerate(nums):
            if count == total - count - n:
                return i
            count += n
        return -1
