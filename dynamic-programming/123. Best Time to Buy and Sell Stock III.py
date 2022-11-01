class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        k = 2
        l = len(prices)

        dp = [[[0 for _ in range(2)] for _ in range(k+1)] for _ in range(l)]
        for e in range(k + 1):
            dp[0][e][0] = 0
            dp[0][e][1] = -prices[0]
        for i in range(1, l):
            for j in range(k, 0, -1):
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])

        return dp[l - 1][k][0]


'''
状态转移方程
T[i][k][0] = max(T[i - 1][k][0], T[i - 1][k][1] + prices[i])
T[i][k][1] = max(T[i - 1][k][1], T[i - 1][k - 1][0] - prices[i])


这一题 k=2
T[i][2][0] = max(T[i - 1][2][0], T[i - 1][2][1] + prices[i])
T[i][2][1] = max(T[i - 1][2][1], T[i - 1][1][0] - prices[i])

# k逐渐变成 1 和 0
T[i][1][0] = max(T[i - 1][1][0], T[i - 1][1][1] + prices[i])
T[i][1][1] = max(T[i - 1][1][1], T[i - 1][0][0] - prices[i]) = max(T[i - 1][1][1], -prices[i])

第一版 
if len(prices)<2:
    return 0

l = len(prices)
dp = [[[0 for _ in range(2)] for _ in range(3)] for _ in range(l)]
dp[0][1][0] = 0
dp[0][1][1] = -prices[0]
dp[0][2][0] = 0
dp[0][2][1] = -prices[0]

for i in range(1, l):
    dp[i][2][0] = max(dp[i - 1][2][0], dp[i - 1][2][1] + prices[i])
    dp[i][2][1] = max(dp[i - 1][2][1], dp[i - 1][1][0] - prices[i])
    dp[i][1][0] = max(dp[i - 1][1][0], dp[i - 1][1][1] + prices[i])
    dp[i][1][1] = max(dp[i - 1][1][1], dp[i - 1][0][0] - prices[i])
return dp[l - 1][2][0]


第二版 
没有第二版了，所有限制都在，没办法删了
'''
