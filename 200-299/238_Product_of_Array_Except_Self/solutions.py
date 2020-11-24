from functools import reduce
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """Product array of dynamic way - O(N) because its count in loop 3N"""
        left_sum, right_sum = [], []

        temp = 1
        for num in nums:
            temp = num*temp
            left_sum.append(temp)

        temp = 1
        for num in nums[::-1]:
            temp = num*temp
            right_sum.append(temp)

        right_sum = right_sum[::-1]

        result = []
        for idx in range(1, len(nums)-1):
            left_val = left_sum[idx-1]
            right_val = right_sum[idx+1]
            result.append(left_val*right_val)

        return [right_sum[1]] + result + [left_sum[len(nums)-2]]

    def product_except_self_short(self, nums: List[int]) -> List[int]:
        """Product array of dynamic way - O(N) because its count in loop 2N"""
        out = []

        p = 1
        # left product
        for i in range(0, len(nums)):
            out.append(p)
            p *= nums[i]

        p = 1
        # right product
        for i in range(len(nums) - 1, 0 - 1, -1):
            out[i] *= p
            p = p * nums[i]

        return out

    def product_except_self_brute_force(self, nums: List[int]) -> List[int]:
        """Product array of brute force way - O(N^2) because its count in loop 3N product list size N"""
        return [reduce((lambda x, y: x * y), nums[:idx] + nums[idx+1:]) for idx in range(len(nums))]


if __name__ == '__main__':
    print(Solution().productExceptSelf([1, 2, 3]))
    print(Solution().productExceptSelf([12, 4, 6, 8]))
