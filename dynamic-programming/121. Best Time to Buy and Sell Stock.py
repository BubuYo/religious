class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        ans = 0
        low = prices[0]
        # 向后遍历一遍价格
        for i in range(1, len(prices)):
            # 记录目前位置的最低价格
            low = min(low, prices[i])
            # 当前新数值减去当前最低价
            ans = max(ans, prices[i] - low)
        return ans
