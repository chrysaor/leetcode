import collections
from typing import List


class Solution:
    def __init__(self):
        self.dp = {}
        self.ans_list = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # used_list = [0] * len(candidates)
        return self.another_score_dp(candidates, target)

    def my_reach_score(self, score: int, point_list: List[int], used_list: List[int]):
        """Find combination sum with recursive approach"""
        key = ''.join(str(item) for item in used_list)

        if key in self.dp or score < 0:
            return 0

        if score == 0 and key not in self.dp:
            self.dp[key] = 0

            target = []
            for idx, item in enumerate(used_list):
                for _ in range(item):
                    target.append(point_list[idx])
            self.ans_list.append(target)
            return 1

        ans = 0
        for idx, point in enumerate(point_list):
            used_list[idx] += 1
            ans += self.my_reach_score(score - point, point_list, used_list)
            used_list[idx] -= 1

        return ans

    def my_reach_score_updated(self, candidates, target, curr_nums):
        """Find combination sum with recursive approach"""
        if target == 0:
            return [curr_nums]

        if len(candidates) == 0 or target <= 0:
            return []

        # Get current candidates
        c = candidates[0]
        sol = self.my_reach_score_updated(candidates[1:], target, curr_nums)
        sol.extend(self.my_reach_score_updated(candidates, target - c, curr_nums + [c]))

        return sol

    def another_score_dp(self, candidates, target):
        """Find combination sum with dynamic programming approach"""
        dp = collections.defaultdict(list)
        dp[0] = [[]]

        candidates.sort()
        # Item in [2, 3, 7]
        for c in candidates:
            # Candidate for a target number
            for t in range(c, target + 1):
                # Because of the default dict, if dp[t-c] doesn't exist, make new default list []
                for comb_t_m_c in dp[t-c]:
                    dp[t].append(comb_t_m_c + [c])

        return dp[target]


print(Solution().combinationSum([2, 3, 7], 122))
