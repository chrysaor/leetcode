import functools

class Solution:
    def numDecodings(self, s: str) -> int:
        return self.top_down_approach(s)

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

    @functools.lru_cache(maxsize=1000)
    def top_down_approach(self, s: str) -> int:
        """Dynamic programming: Bottom-up Approach [Time complexity O(V+E)]"""
        ans = 0

        if len(s) == 1:
            if 0 < int(s) <= 9:
                ans += 1
            return ans

        if len(s) == 2:
            ans = 0
            if 0 < int(s[1]) <= 9:
                ans += 1
            if 10 <= int(s) <= 26:
                ans += 1
            return ans

        return self.top_down_approach(s[1:]) + self.top_down_approach(s[2:]) if s[:2] != '00' else 0


sol = Solution()

print(sol.bootom_up_approach('1123'), sol.top_down_approach('1123'))
print(sol.numDecodings('10'), sol.top_down_approach('10'))
print(sol.numDecodings('2101'), sol.top_down_approach('2101'))
print(sol.numDecodings('10001'), sol.top_down_approach('10001'))
print(sol.numDecodings('00000'), sol.top_down_approach('00000'))
print(sol.numDecodings('50'), sol.top_down_approach('50'))
print(sol.numDecodings('12340505012'), sol.top_down_approach('12340505012'))
print(sol.numDecodings("2611055971756562"), sol.top_down_approach('2611055971756562'))
print(sol.numDecodings("0"), sol.top_down_approach('0'))
