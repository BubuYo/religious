class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        last1, last2 = cost[0], cost[1]
        for i in range(2, len(cost)):
            curr = min(last1, last2) + cost[i]
            last1, last2 = last2, curr
        return min(last1, last2)
