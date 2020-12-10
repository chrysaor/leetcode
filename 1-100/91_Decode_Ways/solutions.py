from functools import lru_cache


class Solution:
    def numDecodings(self, s: str) -> int:
        return self.bootom_up_approach(s)

    def bootom_up_approach(self, s: str) -> int:
        """Dynamic programming: Bottom-up Approach [Time complexity O(N)]"""
        if not s:
            return 0

        dp = [0] * (len(s) + 1)

        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1

        for i in range(2, len(s) + 1):
            if 0 < int(s[i-1:i]) <= 9:
                dp[i] += dp[i-1]
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]

        return dp[len(s)]

    def top_down_approach(self, s: str) -> int:
        """Dynamic programming: Bottom-up Approach [Time complexity O(V+E)]"""
        if len(s) == 0 or s is None:
            return 0

        @lru_cache(maxsize=None)
        def dfs(string):
            # Case of '01', '06' ...
            if len(string) > 0 and string[0] == '0':
                return 0
            # Case of a string is fit to complete
            if string == "" or len(string) == 1:
                return 1
            # Case of target to split, we should split string to one length and two length
            if int(string[0:2]) <= 26:
                first = dfs(string[1:])
                second = dfs(string[2:])
                return first+second
            # Case of '50', '29': It keeps previous split factor because there is only one split ways
            else:
                return dfs(string[1:])

        result_sum = dfs(s)

        return result_sum

    def short_line_approach(self, s):
        """Dynamic programming: Bottom-up Approach [Time complexity O(N)]"""
        v, w, p = 0, int(s > ''), ''
        for d in s:
            # v: prev decode ways, w: current decode ways, d: current target string
            v, w, p = w, (d > '0') * w + (9 < int(p + d) < 27) * v, d
            print(v, w, p)
        return w


sol = Solution()

print(sol.numDecodings('1123'), sol.top_down_approach('1123'))
print(sol.numDecodings('10'), sol.top_down_approach('10'))
print(sol.numDecodings('2101'), sol.top_down_approach('2101'))
print(sol.numDecodings('10001'), sol.top_down_approach('10001'))
print(sol.numDecodings('00000'), sol.top_down_approach('00000'))
print(sol.numDecodings('10010012420101'), sol.short_line_approach('10010012420101'))
print(sol.numDecodings('12340505012'), sol.top_down_approach('12340505012'))
print(sol.numDecodings("0"), sol.top_down_approach('0'))
