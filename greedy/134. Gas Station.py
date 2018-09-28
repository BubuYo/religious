class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        res, ans = 0, 0
        for i in range(len(gas)):
            if res + gas[i] < cost[i]:
                res, ans = 0, i + 1
            else:
                res += gas[i] - cost[i]
        return ans
