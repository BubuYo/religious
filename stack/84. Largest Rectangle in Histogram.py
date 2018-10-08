class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        tmp, stack, ans = heights + [0], [], 0
        for idx, t in enumerate(tmp):
            while stack and t < tmp[stack[-1]]:
                height = tmp[stack.pop()]
                width = idx if not stack else idx - stack[-1] - 1
                ans = max(ans, height * width)
            stack.append(idx)
        return ans
