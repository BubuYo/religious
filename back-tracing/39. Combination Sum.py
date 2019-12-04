class Solution:

    def helper(self, currrent_list, candidates,
               target, current_sum, position):
        if position == len(candidates) and current_sum != target:
            return

        if current_sum == target:
            self.result.append(currrent_list)
            return
        for i in range(position, len(candidates)):
            if current_sum + candidates[i] <= target:
                tmp_list = currrent_list + [candidates[i]]
                self.helper(
                    tmp_list,
                    candidates,
                    target,
                    current_sum +
                    candidates[i],
                    i)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return [[]]
        self.result = []
        self.helper([], candidates, target, 0, 0)
        return self.result
