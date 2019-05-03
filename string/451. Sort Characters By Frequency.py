class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join([i[1]*i[0] for i in sorted([(k,j) for j, k in collections.Counter(s).items()], reverse=True)])
