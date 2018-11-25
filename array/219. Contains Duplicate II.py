class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k < 0 or len(nums) == len(set(nums)):
            return False

        map = {}

        for idx, i in enumerate(nums):
            if i in map and idx - map[i] <= k:
                return True
            map[i] = idx
        return False
