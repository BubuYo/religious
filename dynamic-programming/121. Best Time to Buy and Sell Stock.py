class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        ans = 0
        l = prices[0]
        for i in range(1, len(prices)):
            l = min(l, prices[i])
            ans = max(prices[i] - l, ans)
        return ans
