class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        t = 0
        for i, x in enumerate(nums):
            if x != val:
                if i != t:
                    nums[j] = x
                t += 1
        return t
