from itertools import accumulate
from typing import List


class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        result = [0] * length

        for start, end, val in updates:
            result[start] += val
            if end + 1 < length:
                result[end + 1] += -val
            print(result)
        return list(accumulate(result))

    def naive_approach(self, length: int, updates: List[List[int]]) -> List[int]:
        """Naive approach - T: O(NK) S: O(1), (C++은 통과, 파이썬3 기준 시간 초과 발생)"""
        result = [0] * length

        for start, end, val in updates:
            for idx in range(start, end + 1):
                result[idx] += val

        return result


print(Solution().getModifiedArray(5, [[1, 3, 2], [2, 4, 3], [0, 2, -2]]))
print(Solution().naive_approach(5, [[1, 3, 2], [2, 4, 3], [0, 2, -2]]))
