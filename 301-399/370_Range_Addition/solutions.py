from typing import List


class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        pass

    @classmethod
    def divide_arr(cls, target_item, target_list):
        """
        새로운 배열이 들어오면 기존 배열과 비교하여 적정 범위로 쪼갠다.
        Args:
            target_item: List[int] -> [1, 2999, 10]
            target_list: List[List[int]] -> [[1, 2999, 10], [2, 5, -5]]

        Returns:
            List[List[int]]
        """
        t_start = target_item[0]
        t_end = target_item[1]
        t_val = target_item[2]

        updated_list = []

        for item in target_list:
            item_start = item[0]
            item_end = item[1]
            item_val = item[2]

            # Ignore case
            if t_end < item_start or t_start > item_end:
                continue

            # Case 1. 대상의 끝 위치 보다 현재 아이템의 시작이 작은 경우
