class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        return self.solve_with_stack(s)

    @classmethod
    def solve_with_stack(cls, s: str) -> str:
        """
        Stack을 이용한 풀이법
        Key idea: () 연산이 안되는 경우 index를 기록하여 해당 index로 string을 재구성

        Time Complexity: O(N)
        Space Complexity: O(N)

        :param s: (,)가 포함된 문자열
        :return: 불필요한 괄호가 제거된 문자열
        """
        path_list = []

        for idx, item in enumerate(list(s)):
            # 닫히는 케이스
            if item == ')':
                if len(path_list) == 0 or path_list[-1][0] != '(':
                    path_list.append((')', idx))
                elif path_list[-1][0] == '(':
                    path_list.pop()

            # 열리는 케이스
            if item == '(':
                path_list.append(('(', idx))

        idx_set = set()
        for item in path_list:
            idx_set.add(item[1])

        result = []
        for idx, item in enumerate(list(s)):
            if idx not in idx_set:
                result.append(item)

        return ''.join(result)

    @classmethod
    def solve_with_stack2(cls, s: str) -> str:
        """
        Stack을 이용한 풀이법
        Key idea: () 연산이 안되는 경우 index를 기록하여 해당 index로 string을 재구성

        Time Complexity: O(N)
        Space Complexity: O(N)

        :param s: (,)가 포함된 문자열
        :return: 불필요한 괄호가 제거된 문자열
        """
        indexes_to_remove = set()
        stack = []
        for i, c in enumerate(s):
            if c not in '()':
                continue
            if c == '(':
                stack.append(i)
            elif not stack:
                indexes_to_remove.add(i)
            else:
                stack.pop()

        indexes_to_remove = indexes_to_remove.union(set(stack))

        string_builder = []
        for i, c in enumerate(s):
            if i not in indexes_to_remove:
                string_builder.append(c)
        return ''.join(string_builder)
