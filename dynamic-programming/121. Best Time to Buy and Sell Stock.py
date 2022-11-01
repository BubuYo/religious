class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        p0 = 0
        p1 = -prices[0]
        for i in range(1, len(prices)):
            p0 = max(p0, p1 + prices[i])
            p1 = max(p1, -prices[i])
        return p0


'''
状态转移方程
T[i][k][0] = max(T[i - 1][k][0], T[i - 1][k][1] + prices[i])
T[i][k][1] = max(T[i - 1][k][1], T[i - 1][k - 1][0] - prices[i])


这一题 k=1
T[i][1][0] = max(T[i - 1][1][0], T[i - 1][1][1] + prices[i])
T[i][1][1] = max(T[i - 1][1][1], T[i - 1][0][0] - prices[i]) = max(T[i - 1][1][1], -prices[i])



第一版 删掉k
if len(prices)<2:
    return 0

l = len(prices)
dp = [[0 for _ in range(l)] for _ in range(l)]
dp[0][0] = 0
dp[0][1] = -prices[0]
for i in range(1, l):
    dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
    dp[i][1] = max(dp[i - 1][1], -prices[i])
return dp[l - 1][0]


第二版 删掉 i
p0=0
p1=-prices[0]
for i in range(1, len(prices)):
    p0 = max(p0, p1 + prices[i])
    p1 = max(p1, -prices[i])
return p0
'''
