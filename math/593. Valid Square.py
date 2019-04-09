class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def dis(a, b):
            return (a[0] - b[0])**2 + (a[1] - b[1])**2

        tmp = [dis(p1, p2), dis(p1, p3), dis(p1, p4), dis(p2, p3), dis(p2, p4), dis(p3, p4)]
        tmp.sort()

        return bool(tmp[0] and tmp[0] == tmp[3] and tmp[4] == tmp[5])
