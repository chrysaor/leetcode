class Solution:
    def __init__(self):
        self.dp = {}
        self.ans_list = []

    def totalWaysToReachScore(self, finalScore, pointEvents):
        '''
        :type finalScore: int
        :type pointEvents: list of int
        :rtype: int
        '''
        used_list = [0] * len(pointEvents)
        res = self.reach_score(finalScore, pointEvents, used_list)
        print(self.ans_list)
        return res

    def reach_score(self, score, point_list, used_list):
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
            ans += self.reach_score(score - point, point_list, used_list)
            used_list[idx] -= 1

        self.dp[key] = ans

        return ans


print(Solution().totalWaysToReachScore(12, [2, 3, 7]))
