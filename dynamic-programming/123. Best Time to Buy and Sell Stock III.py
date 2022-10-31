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


class Solution2:
    def maxProfit(self, prices) -> int:
        n = len(prices)
        left = [0] * n
        right = [0] * n
        minl = prices[0]
        maxr = prices[-1]
        for i in range(1, n):
            minl = min(minl, prices[i])
            left[i] = max(left[i - 1], prices[i] - minl)
            j = n - i - 1
            maxr = max(maxr, prices[j])
            right[j] = max(right[j + 1], maxr - prices[j])
        print(left, right)

        profit = right[0]
        for i in range(1, n):
            profit = max(profit, left[i - 1] + right[i])
        return profit


if __name__ == '__main__':
    a = Solution2()
    a.maxProfit([3, 3, 5, 0, 0, 3, 1, 4])
