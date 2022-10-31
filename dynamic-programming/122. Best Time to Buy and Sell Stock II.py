# 思路：跌时，收取涨的收益

# 逢跌则加 ans 增量，并设置 l 为当前下跌处
# 如果最后几个元素都是上升，则可以购买卖出获利，还需要再加上


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        l = prices[0]
        ans = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[i - 1]:
                ans += prices[i - 1] - l
                l = prices[i]

        return ans + max(prices[-1] - l, 0)
