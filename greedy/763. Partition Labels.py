class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """

        used, ans = {}, []
        for index, i in enumerate(S):
            if i not in used:
                used[i] = [index, index]
            else:
                used[i][1] = index
        tmp = sorted(used.values())
        start, end = tmp[0]
        for j, k in tmp[1:]:
            if j > end:
                ans.append(end - start + 1)
                start, end = j, k
            end = max(end, k)
        ans.append(end - start + 1)
        return ans
