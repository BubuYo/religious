# Given two strings s and t , write a function to determine if t is an anagram of s.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        ss = list(s)
        ss.sort()
        tt = list(t)
        tt.sort()
        return ss == tt


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return all(s.count(c) == t.count(c) for c in "abcdefghijklmnopqrstuvwxyz")
