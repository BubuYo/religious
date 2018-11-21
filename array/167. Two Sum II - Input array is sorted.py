class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}

        for i, n in enumerate(numbers):
            if target - n in map:
                return [map[target - n], i + 1]
            else:
                map[n] = i + 1
