from itertools import accumulate
from typing import List


class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        return self.accumulate_solution(length, updates)

    @classmethod
    def accumulate_solution(cls, length: int, updates: List[List[int]]) -> List[int]:
        """
        배열을 미리 계산하여 범위 덧셈을 구한다. (효율적인 방법)

        시간 복잡도: O(N)
        공간 복잡도: O(length)

        Args:
            length:
                주어진 range 배열의 길이 (10개: [0, 0, 0, ..., 0]
            updates:
                range 배열에 업데이트 해야할 값들 [ [0, 2, 1], ... ]
                [0, 2, 1]은 range 배열의 0~2까지 값 1을 더하라는 의미

        Returns:
            array (List[int]): 계산된 range 배열의 값 [0, -1, 2, ..., 3]
        """
        result = [0] * length

        for start, end, val in updates:
            result[start] += val
            if end + 1 < length:
                result[end + 1] += -val
            print(result)

        return list(accumulate(result))

    @classmethod
    def naive_approach(cls, length: int, updates: List[List[int]]) -> List[int]:
        """
        배열을 미리 계산하여 범위 덧셈을 구한다. (느슨한 방법)
        C++의 경우 속도 때문에 느슨한 방법도 통과.
        하지만 파이썬3 기준 시간초과 발생함을 고려 할 것

        시간 복잡도: O(NK)
        공간 복잡도: O(1)

        Args:
            length:
                주어진 range 배열의 길이 (10개: [0, 0, 0, ..., 0]
            updates:
                range 배열에 업데이트 해야할 값들 [ [0, 2, 1], ... ]
                [0, 2, 1]은 range 배열의 0~2까지 값 1을 더하라는 의미
        """
        result = [0] * length

        for start, end, val in updates:
            for idx in range(start, end + 1):
                result[idx] += val

        return result


if __name__ == '__main__':
    print(Solution().getModifiedArray(5, [[1, 3, 2], [2, 4, 3], [0, 2, -2]]))
    print(Solution().naive_approach(5, [[1, 3, 2], [2, 4, 3], [0, 2, -2]]))
