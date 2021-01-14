class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # only put unique num within nums[:i+1]
        # other num not remove to make it into O(1)
        if not nums:
            return 0
        i = 0  # slow pointer
        for j in range(1, len(nums)):
            # j: quick pointer
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
                print(nums)
        return i + 1
