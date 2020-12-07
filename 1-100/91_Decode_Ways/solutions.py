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
        pass


print(Solution().numDecodings('1123'))
print(Solution().numDecodings('10'))
print(Solution().numDecodings('2101'))
print(Solution().numDecodings('10001'))
print(Solution().numDecodings('00000'))
print(Solution().numDecodings('50'))
print(Solution().numDecodings('27'))
print(Solution().numDecodings('0'))
print(Solution().numDecodings("2611055971756562"))
