from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        print(coins, amount)
        return -1

    @classmethod
    def bottom_up(cls, coins: List[int], amount: int) -> int:
        # Bottom up DP 배열 초기화
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        print('Initial DP array: ', dp)

        # 거스름돈 금액까지 반복 O(S*coin)
        for idx in range(1, amount + 1):
            # 각 코인별 모든 상황 비교 후 가장 작은 값으로 교체
            for coin in coins:
                # 거스름돈을 넘어서는 코인은 체크하지 않음
                if idx >= coin:
                    # 코인별 sub-problem 을 참고하여 가장 작은 값을 구한다.
                    dp[idx] = min(dp[idx], dp[idx - coin] + 1)

        print('result DP array: ', dp)
        return dp[amount] if dp[amount] != amount + 1 else -1


if __name__ == '__main__':
    print(Solution.bottom_up([1, 2, 5], 11))
