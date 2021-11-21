import itertools
from collections import defaultdict


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        return Solution.count_binary(s)

    @classmethod
    def count_binary(cls, s: str) -> int:
        """
        1과 0으로 이루어진 부분 문자열의 개수를 센다.

        key idea:
        문자열을 순차적으로 탐색하면서 카운팅, 패턴이 바뀌는 경우 (1 -> 0, 0 -> 1)
        바뀐 패턴의 갯수를 카운팅하여 두 숫자중 작은 숫자를 더해준다.
        이후 다시 시작할 인덱스를 설정해주고 반복

        시간 복잡도: O(N)
        공간 복잡도: O(1)

        Args:
            s: 0과 1로 이루어진 문자열

        Returns:
            int: 01, 1100, 10 ... - 0과 1로 연결된 부문 문자열의 갯수
        """
        result = 0
        idx = 0
        ch = s[0]

        cnt_map = defaultdict(int)

        while idx < len(s):
            if s[idx] == ch:
                cnt_map[ch] += 1
            else:
                # 다른 케이스
                curr = s[idx]
                for i in range(idx, len(s)):
                    if s[i] == curr:
                        cnt_map[curr] += 1
                    else:
                        break

                # 값들 정리
                result += min(cnt_map['0'], cnt_map['1'])
                cnt_map['0'] = 0
                cnt_map['1'] = 0
                ch = curr
                continue

            idx += 1

        return result

    @classmethod
    def group_solution(cls, s: str) -> int:
        """
        1과 0으로 이루어진 부분 문자열의 개수를 센다.

        key idea:
        문자열이 바뀌는 지점을 그룹화하여 해당 그룹의 합을 구한다.

        시간 복잡도: O(N)
        공간 복잡도: O(1)

        Args:
            s: 0과 1로 이루어진 문자열

        Returns:
            int: 01, 1100, 10 ... - 0과 1로 연결된 부문 문자열의 갯수
        """
        groups = [1]
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                groups.append(1)
            else:
                groups[-1] += 1

        ans = 0
        for i in range(1, len(groups)):
            ans += min(groups[i-1], groups[i])
        return ans

    @classmethod
    def two_line_solution(cls, s: str) -> int:
        groups = [len(list(v)) for _, v in itertools.groupby(s)]
        return sum(min(a, b) for a, b in zip(groups, groups[1:]))

    @classmethod
    def linear_solution(cls, s: str) -> int:
        ans, prev, cur = 0, 0, 1
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                ans += min(prev, cur)
                prev, cur = cur, 1
            else:
                cur += 1

        return ans + min(prev, cur)
