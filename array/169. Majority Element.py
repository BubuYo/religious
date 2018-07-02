class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        L = len(nums) // 2
        a = Counter(nums)
        for i in nums:
            if a[i] > L:
                return i
