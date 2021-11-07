from collections import Counter
from functools import reduce
from operator import xor
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Single number 구하기

        입력된 리스트의 정수값중 1번만 나온 정수 값을 찾는다.
        bit mask 방법을 사용해야 공간복잡도는 O(1)이 가능하다.

        Time complexity: O(N)
        Space complexity: O(N)

        :param nums: 정수값 리스트
        :return: 1번만 출현한 정수값
        """
        counter = Counter(nums)

        for item in counter.items():
            if item[1] == 1:
                return item[0]

    @classmethod
    def math_approach(cls, nums: List[int]) -> int:
        """
        Single number 구하기 (수학적 접근)

        Key idea
        - 2 * (a + b + c) - (a + a + b + b + c) = c임을 이용

        Time complexity: O(N)
        Space complexity: O(N)

        :param nums: 정수값 리스트
        :return: 1번만 출현한 정수값
        """
        return 2 * sum(set(nums)) - sum(nums)

    @classmethod
    def bit_manipulation(cls, nums: List[int]) -> int:
        """
        Single number 구하기 (bit mask 방법)

        Key idea
        - XOR값 연산을 통해 유일한 정수값을 구함
        - a xor 0 = a
        - a xor a = 0
        - a xor b xor a = (a xor a) xor b = 0

        Time complexity: O(N)
        Space complexity: O(1)

        :param nums: 정수값 리스트
        :return: 1번만 출현한 정수값
        """
        a = 0
        for num in nums:
            # a xor number
            a ^= num

        return a

    @classmethod
    def one_line_solutions(cls, nums: List[int]) -> int:
        """
        Single number 구하기 (bit mask 방법, 한줄 간소화)

        Key idea
        - XOR값 연산을 통해 유일한 정수값을 구함
        - a xor 0 = a
        - a xor a = 0
        - a xor b xor a = (a xor a) xor b = 0

        Time complexity: O(N)
        Space complexity: O(1)

        :param nums: 정수값 리스트
        :return: 1번만 출현한 정수값
        """
        return reduce(xor, nums, 0)
