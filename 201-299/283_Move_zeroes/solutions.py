from typing import List


class Solution:
    @classmethod
    def move_zeros(cls, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        This solution : T(N), O(1)
        """
        last_idx = 0

        for idx in range(len(nums)):
            if nums[idx] != 0 and nums[last_idx] == 0:
                nums[last_idx], nums[idx] = nums[idx], nums[last_idx]

            if nums[last_idx] != 0:
                last_idx += 1

    @classmethod
    def two_pointers_technique(cls, nums: List[int]) -> None:
        """More simple solution

        :param nums: List[int]
        :return: None
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
