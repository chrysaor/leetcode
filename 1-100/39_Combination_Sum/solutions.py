from typing import List


class Solution:
    def __init__(self):
        self.dp = {}
        self.current = {}
        self.ans_list = []

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        used_list = [0] * len(candidates)
        self.my_reach_score(target, candidates, used_list)
        return self.ans_list

    def my_reach_score(self, score: int, point_list: List[int], used_list: List[int]):
        """Find combination sum with DP"""
        key = ','.join(str(item) for item in used_list)

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

        self.dp[key] = ans

        return ans


print(Solution().combinationSum([2, 3, 7], 12))
