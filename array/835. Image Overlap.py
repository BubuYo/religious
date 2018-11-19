class Solution:
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        map = collections.defaultdict(int)
        A1 = [complex(j, k) for j, l in enumerate(A) for k, v in enumerate(l) if v]
        B1 = [complex(j, k) for j, l in enumerate(B) for k, v in enumerate(l) if v]
        
        for j in A1:
            for k in B1:
                map[j-k] += 1
        return max(map.values() or [0])
