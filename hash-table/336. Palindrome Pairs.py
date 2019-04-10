class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        d, res = dict([(w[::-1], i) for i, w in enumerate(words)]), []
        for i, w in enumerate(words):
            for j in range(len(w) + 1):
                prefix, postfix = w[:j], w[j:]
                if prefix in d and i != d[prefix] and postfix == postfix[::-1]:
                    res.append([i, d[prefix]])
                if j > 0 and postfix in d and i != d[postfix] and prefix == prefix[::-1]:
                    res.append([d[postfix], i])
        return res
