import sys

from functools import lru_cache
from typing import List


class Solution:
    def __init__(self) -> None:
        # 기본 설정(1000) 오류 방지용 recursion limit 해제
        sys.setrecursionlimit(30000)
        self.inf_val = 10**4 + 1
        self.unavailable = -1

    def coin_change(self, coins: List[int], amount: int) -> int:
        print(coins, amount)
        return self.top_down(coins, amount)

    def top_down(self, coins: List[int], amount: int) -> int:
        """TOP-DOWN 방식으로 구현"""
        # lru_cache: 파라미터와 함수 결과값 메모이제이션용 데코레이터
        @lru_cache(None)
        def exchange(amt: int) -> int:
            """거스름돈으로 바꿀 수 있는 가장 작은 수의 동전을 반환"""
            if amt < 0:
                return self.inf_val  # 거스름돈 교환이 불가능한 경우, 최대 입력값 10^4
            if amt == 0:
                return 0  # 남은 거스름돈 만큼 교환된 경우

            # 현재 선택한 동전 + 나머지 금액의 동전별 사용 갯수 중 최소 값
            return 1 + min(exchange(amt - coin) for coin in coins)

        return exchange(amount) if exchange(amount) < self.inf_val else self.unavailable

    def bottom_up(self, coins: List[int], amount: int) -> int:
        """BOTTOM-UP 방식으로 구현"""
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
        return dp[amount] if dp[amount] != amount + 1 else self.unavailable


if __name__ == '__main__':
    print(Solution().bottom_up([1, 2, 5], 14))
