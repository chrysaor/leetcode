from typing import List


class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        result = [0] * length

        # [[1,3,2],[2,4,3],[0,2,-2]]
        result_list = updates.copy()
        for idx in range(1, len(updates)):
            divide = Solution.divide_arr(result_list[idx - 1], result_list[idx])
            result_list = divide + result_list[idx:]

        s_list = sorted(result_list, key=lambda x: x[0])
        for idx, item in enumerate(s_list):
            if item[0] <= idx <= item[1]:
                result[idx] = item[2]

        return result

    @classmethod
    def divide_arr(cls, target_item, origin_item):
        """
        새로운 배열이 들어오면 기존 배열과 비교하여 적정 범위로 쪼갠다.
        Args:
            target_item: List[int] -> [1, 2999, 10]
            origin_item: List[int] -> [2, 5, -5]

        Returns:
            List[List[int]]
        """
        t_start = target_item[0]
        t_end = target_item[1]
        t_val = target_item[2]

        updated_list = []

        item_start = origin_item[0]
        item_end = origin_item[1]
        item_val = origin_item[2]

        if t_start > item_end or item_start > t_end:
            updated_list.append(origin_item)
            updated_list.append(target_item)
            return updated_list

        # Case 0. 대상의 범위가 같은 경우
        if t_start == item_start and t_end == item_end:
            return [item_start, item_end, t_val + item_val]

        # Case 1. 왼쪽 겹침
        if t_start == item_start and t_end > item_end:
            return [[t_start, item_end, t_val + item_val], [item_end + 1, t_end, t_val]]

        # Case 2. 오른쪽 겹침
        if t_end == item_end and t_start < item_start:
            return [[t_start, item_start, t_val], [item_start + 1, t_end, t_val + item_val]]

        # Other case. index, value 로 pairing
        tuple_list = [
            (t_start, t_val), (t_end, t_val),
            (item_start, item_val), (item_end, item_val)
        ]
        s_list = sorted(tuple_list, key=lambda x: x[0])
        return [
            [s_list[0][0], s_list[1][0], s_list[0][1]],
            [s_list[1][0] + 1, s_list[2][0], s_list[1][1] + s_list[2][1]],
            [s_list[2][0] + 1, s_list[3][0], s_list[3][1]]
        ]


print(Solution().getModifiedArray(5, [[1,3,2],[2,4,3],[0,2,-2]]))
