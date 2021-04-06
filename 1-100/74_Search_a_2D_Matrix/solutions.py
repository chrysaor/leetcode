from bisect import bisect_left
from typing import List


class Solution:
    @classmethod
    def list_binary_search(cls, target_list: List[int], target_value: int) -> bool:
        """Python binary search solution

        :param target_list: Target integer list
        :param target_value: Search value
        :return: Target find result bool value
        """
        idx = bisect_left(target_list, target_value)
        if idx != len(target_list) and target_list[idx] == target_value:
            return True
        else:
            return False

    @classmethod
    def search_matrix(cls, matrix: List[List[int]], target: int) -> bool:
        """Python simple solution"""
        target_list = []
        for idx in range(len(matrix)):
            target_list += matrix[idx]

        return target in target_list
