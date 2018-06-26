class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        result, n = 0, len(A)
        sum_count = collections.defaultdict(int)

        for i in range(n):
            for j in range(n):
                sum_count[A[i] + B[j]] += 1
        for i in range(n):
            for j in range(n):
                tmp = C[i] + D[j]
                result += sum_count[-tmp]
        return result
