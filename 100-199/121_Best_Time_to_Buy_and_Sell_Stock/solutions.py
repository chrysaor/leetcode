from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Calculate max profit with the dynamic programming"""
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


print(Solution().maxProfit([3, 2, 6, 5, 0, 3]))
print(Solution().maxProfit([12, 4, 6, 9, 3, 8, 4]))
print(Solution().maxProfit([6, 5, 4, 3, 2, 1]))
