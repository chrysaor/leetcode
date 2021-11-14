import collections


class Solution:
    def countLargestGroup(self, n: int) -> int:
        return self.solve_with_dp(n)

    @classmethod
    def solve_with_dp(cls, n: int) -> int:
        """
        DP를 이용한 풀이법
        Key idea:
        DP 배열에 각 숫자별 그룹 길이를 기록, Counts 배열에 길이를 누적
        결과적으로 Counts 배열 에서 가장 긴 길이를 뽑고 이 숫자를 counting 하여 반환
        counts 배열은 최대 9999의 숫자를

        Time Complexity: O(N)
        Space Complexity: O(N)

        :param n: N번째 숫자
        :return: N까지 숫자들중 각 자리의 수를 더한 수가 같은 가장 긴 그룹의 길이를 리턴
        """
        dp = {0: 0}
        counts = [0] * (4 * 9)
        for i in range(1, n + 1):
            quotient, reminder = divmod(i, 10)
            dp[i] = reminder + dp[quotient]
            counts[dp[i] - 1] += 1

        return counts.count(max(counts))

    @classmethod
    def solve_with_counter(cls, n: int) -> int:
        """
        Counter 풀이법
        Key idea:
        counter에 해당 길이 조합을 계산
        예) n = 13
        1, 2, 3, 4, ... -> 1, 2, 3, 4 ...
        => Counter(1: 2, 2: 2:, 3: 2, 4: 2, 5: 1, ...)

        Time Complexity: O(N)
        Space Complexity: O(N)

        :param n: N번째 숫자
        :return: N까지 숫자들중 각 자리의 수를 더한 수가 같은 가장 긴 그룹의 길이를 리턴
        """
        group = collections.Counter(map(lambda x: sum(map(int, str(x))), range(1, n + 1)))
        mx = max(group.values())
        return sum(v == mx for k, v in group.items())
