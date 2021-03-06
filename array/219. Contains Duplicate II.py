class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l, remain = len(nums), 0
        for idx, i in enumerate(nums):
            if idx + i + 1 >= l:
                return True
            remain = max(i, remain - 1)
            if not any([i, remain]):
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    nums = [3, 2, 1, 0, 4]
    a = s.canJump(nums)
    print(a)
