class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        ans, length = [], len(set(pattern))
        def match_length(word):
            return len(set(word)) == length
        for word in filter(match_length, words):
            tmp, matched = {}, True
            for i, w in enumerate(word):
                if w not in tmp:
                    tmp[w] = pattern[i]
                elif pattern[i] != tmp[w]:
                    matched = False
                    break
            if matched:
                ans.append(word)
        return ans
