class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        current = 0

        for item in list(p):
            if item == '*':
                # s = "mississippi", p = "mis*is*p*."

                pass
            elif item == '.':
                if current < len(s) - 1:
                    return False
                current += 1
            else:
                # 일반 문자열
                if item != current:
                    return False
                current += 1

        return True
