    class Solution:
        def helper(self, current_list, candidates, current_sum, target, position,used_positions):
            if position == len(candidates) and current_sum < target:
                return

            if current_sum == target:
                current_list.sort()
                s = ','.join([str(c) for c in current_list])
                if s not in self.result:
                    self.result.append(s)
                return

            for i in range(position, len(candidates)):
                next_sum = current_sum + candidates[i]
                if next_sum <= target and i not in used_positions:
                    self.helper(
                        current_list + [candidates[i]],
                        candidates,
                        next_sum,
                        target,
                        position+1,  # 和 39 题的区别
                        used_positions+[i]  # 和 39 题的区别
                        )
                

        def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
            if not candidates:
                return [[]]
            self.result = []
            sorted_candidates = sorted(candidates)
            self.helper([], candidates, 0, target, 0, [])
            return [i.split(',') for i in self.result]
