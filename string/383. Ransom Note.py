class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        r = collections.Counter(ransomNote)
        m = collections.Counter(magazine)

        for k, v in r.items():
            if m[k] < v:
                return False
        return True
