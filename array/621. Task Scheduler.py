class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        infs = collections.Counter(tasks)
        freq = max(infs.values())
        nMax = sum(infs[let] == freq for let in infs)
        return max(len(tasks), ((n + 1) * (freq - 1)) + nMax)
