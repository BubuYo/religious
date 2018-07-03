class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) == 1:
            return True
        if word.lower() == word:
            return True
        if word.upper() == word:
            return True
        if word[0] == word[0].upper() and word[1:] == word[1:].lower():
            return True
        return False
