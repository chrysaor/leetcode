from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Calculate max profit with the min max calculation"""
        if prices is None or len(prices) <= 1:
            return 0

        max_idx = 0
        max_res = 0

        # O(N): Loop for all prices
        for idx in range(1, len(prices)):
            if prices[idx] - prices[idx-1] > prices[idx] - prices[max_idx]:
                max_res = max(prices[idx] - prices[idx-1], max_res)
                max_idx = idx - 1
            else:
                max_res = max(prices[idx] - prices[max_idx], max_res)

        return max(max_res, 0)

    def maxProfitDp(self, prices: List[int]) -> int:
        """Calculate max profit with the dynamic programming"""
        if prices is None or len(prices) <= 1:
            return 0

        optimal = [0] * len(prices)

        # O(N): Loop for all prices
        # OPT[IDX] = max(0, OPT[IDX-1] + TODAY_EARNING)
        for idx in range(1, len(prices)):
            today_earn = prices[idx] - prices[idx-1]
            optimal[idx] = max(0, optimal[idx-1] + today_earn)

        return max(optimal)


print(Solution().maxProfitDp([2, 1]))
print(Solution().maxProfitDp([12, 4, 6, 9, 3, 8, 4]))
print(Solution().maxProfitDp([6, 5, 4, 3, 2, 1]))
