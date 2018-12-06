class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = collections.Counter(nums)
        ans = 0
        for k, v in counter.items():
            if k + 1 in counter:
                ans = max(ans, v + counter[k + 1])
        return ans
