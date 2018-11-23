class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [k for k, v in collections.Counter(nums).items() if v == 1]


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = set()
        for i in nums:
            if i in ans:
                ans.remove(i)
            else:
                ans.add(i)
        return list(ans)
