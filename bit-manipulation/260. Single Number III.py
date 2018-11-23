class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [k for k, v in collections.Counter(nums).items() if v == 1]