from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        print(coins, amount)
        return -1

    def brute_force(self, coins: List[int], amount: int) -> int:
        r_coins = sorted(coins)[::-1]
        return -1


if __name__ == '__main__':
    print(Solution().coinChange([1, 3, 5], 11))
