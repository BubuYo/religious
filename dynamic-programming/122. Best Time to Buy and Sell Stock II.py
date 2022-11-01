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
        p0 = 0
        p1 = -prices[0]
        for i in range(1, len(prices)):
            p0 = max(p0, p1 + prices[i])
            p1 = max(p1, p0 - prices[i])  # 和上一题唯一区别就是多了个 p0
        return p0


'''
状态转移方程
T[i][k][0] = max(T[i - 1][k][0], T[i - 1][k][1] + prices[i])
T[i][k][1] = max(T[i - 1][k][1], T[i - 1][k - 1][0] - prices[i])


这一题 k=正无穷，k=k-1
T[i][k][0] = max(T[i - 1][k][0], T[i - 1][k][1] + prices[i])
T[i][k][1] = max(T[i - 1][k][1], T[i - 1][k][0] - prices[i])


第一版 
if len(prices)<2:
    return 0

l = len(prices)
dp = [[0 for _ in range(l)] for _ in range(l)]
dp[0][0] = 0
dp[0][1] = -prices[0]
for i in range(1, l):
    dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
    dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i]) # 和上一题唯一区别就是多了个 dp[i - 1][0]
return dp[l - 1][0]


第二版 
第i天的最大收益只和第i - 1天的最大收益相关
p1 记录到 i 时的最小值（负数然后取最大 相当于取最小）
p0 记录当前 i 处价格减去当前的 p1 的值，最终留下最大的 p0
p0=0
p1=-prices[0]
for i in range(1, len(prices)):
    p0 = max(p0, p1 + prices[i])
    p1 = max(p1, p0-prices[i]) # 和上一题唯一区别就是多了个 p0
return p0
'''
