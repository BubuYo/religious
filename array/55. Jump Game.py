class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length, remain = len(nums), 0
        for idx, i in enumerate(nums):
            if idx + i + 1 >= length:
                return True
            remain = max(i, remain - 1)
            if not any([i, remain]):
                return False
        return True
