class Solution:
    def maxProfit(self, prices) -> int:
        if not prices:
            return 0
        l = prices[0]
        ans = []
        for i in range(1, len(prices)):
            if prices[i] < prices[i - 1]:
                ans.append(prices[i - 1] - l)
                l = prices[i]
        ans.append(max(prices[-1] - l, 0))
        ans.sort(reverse=True)
        return sum(ans[:2])  # 失败，因为出现新情况：1324时，13 24 两次截取, 但是因为只能截取两次交易，所以只能是 14，不能只取到 13 和 24



