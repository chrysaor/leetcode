from collections import Counter
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        """
        1번씩만 출현한 정수값을 찾아서 반환한다.

        Time complexity: O(N)
        Space complexity: O(N)

        :param nums: 정수값 리스트
        :return: 1번씩만 출현한 숫자 리스트
        """
        num_set = set()

        for item in nums:
            if item not in num_set:
                num_set.add(item)
            else:
                num_set.remove(item)

        return list(num_set)

    @classmethod
    def single_number(cls, nums: List[int]) -> List[int]:
        """
        1번씩만 출현한 정수값을 찾아서 반환한다.

        Time complexity: O(N)
        Space complexity: O(N)

        :param nums: 정수값 리스트
        :return: 1번씩만 출현한 숫자 리스트
        """
        counter = Counter(nums)
        return [x for x in counter if counter[x] == 1]

    @classmethod
    def bit_mask(cls, nums: List[int]) -> List[int]:
        """
        1번씩만 출현한 정수값을 찾아서 반환한다. 비트마스크 방법

        Time complexity: O(N)
        Space complexity: O(1)

        :param nums: 정수값 리스트
        :return: 1번씩만 출현한 숫자 리스트
        """
        # difference between two numbers (x and y) which were seen only once
        bitmask = 0
        for num in nums:
            bitmask ^= num
        print(bitmask)

        # rightmost 1-bit diff between x and y
        diff = bitmask & (-bitmask)

        x = 0
        for num in nums:
            # bitmask which will contain only x
            if num & diff:
                x ^= num

        return [x, bitmask ^ x]
