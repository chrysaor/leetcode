from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
        쿠키를 아이들의 영양 사이즈에 맞게 배분한다.

        Key idea: 영양 사이즈, 쿠키 사이즈를 정렬 후 알맞게 배분한다.

        Time complexity: O(N)
        Space complexity: O(N)

        Args:
            g: 아이들이 수용할 수 있는 영양 사이즈
            s: 쿠키 사이즈

        Returns:
            integer: 아이들에게 맞게 분배된 쿠키의 개수
        """
        g_sorted = sorted(g)
        s_sorted = sorted(s)

        g_idx, result = 0, 0

        for cookie in s_sorted:
            if g_idx >= len(g):
                break

            if cookie >= g_sorted[g_idx]:
                g_idx += 1
                result += 1

        return result
