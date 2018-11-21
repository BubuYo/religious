class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        ans = ['']
        for i in S:
            ans = [a + char for a in ans for char in [i.upper(), i.lower()]] if i.isalpha() else [a + i for a in ans]
        return ans
