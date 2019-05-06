class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        l, r = [], []
        for i in A:
            if i & 1 == 0:
                l.append(i)
            else:
                r.append(i)
        return l + r
