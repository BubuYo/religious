class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp is uesd to record if s[:index] can break
        dp = [1] + [0] * len(s)
        for j in range(len(s) + 1):
            for k in range(j):
                if dp[k] and s[k:j] in wordDict:
                    dp[j] = True
        return dp[-1]
