class Solution:
    def get_letters(self, i):
        if i < 7:
            return chr(3 * i + 91) + chr(3 * i + 92) + chr(3 * i + 93)
        if i == 7:
            return 'pqrs'
        if i == 8:
            return 'tuv'
        return 'wxyz'

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        if len(digits) == 1:
            return list(self.get_letters(int(digits[0])))
        return [j + k for j in self.letterCombinations(digits[:-1]) for k in self.letterCombinations(digits[-1])]
