class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices) < 2:
            return 0

        l = len(prices)
        dp = [[0 for _ in range(l)] for _ in range(l)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, l):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[l - 1][0]


'''
第二题
T[i][k][0] = max(T[i - 1][k][0], T[i - 1][k][1] + prices[i])
T[i][k][1] = max(T[i - 1][k][1], T[i - 1][k][0] - prices[i])


这一题加入了手续费，按卖出时收取
T[i][k][0] = max(T[i - 1][k][0], T[i - 1][k][1] + prices[i] - fee)
T[i][k][1] = max(T[i - 1][k][1], T[i - 1][k][0] - prices[i])

第一版 
见代码

第二版
前面的 Memory Limit Exceeded
需要优化空间复杂度到 O(1)，参考第二题的第二版
p0=0
p1=-prices[0]
for i in range(1, len(prices)):
    p0 = max(p0, p1 + prices[i]-fee)
    p1 = max(p1, p0-prices[i])
return p0
'''
