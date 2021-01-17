class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}

        for idx, v in enumerate(numbers):
            if target - v in map:
                return [map[target - v] + 1, idx + 1]
            map[v] = idx
