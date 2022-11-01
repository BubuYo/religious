class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        l = len(prices)
        dp = [[0 for _ in range(l)] for _ in range(l)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, l):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])
        return dp[l - 1][0]


'''
第二题
T[i][k][0] = max(T[i - 1][k][0], T[i - 1][k][1] + prices[i])
T[i][k][1] = max(T[i - 1][k][1], T[i - 1][k][0] - prices[i])


这一题加入了冷却期
如果在第 i - 1 天卖出了股票，就不能在第 i 天买入股票

T[i][k][0] = max(T[i - 1][k][0], T[i - 1][k][1] + prices[i])
T[i][k][1] = max(T[i - 1][k][1], T[i - 2][k][0] - prices[i])
'''
