from typing import List

from Algorithm.Graph.UnionFind.UnionFind import UnionFind


class Solution:
    def __init__(self):
        self.ans = set()

    def find_circle_num(self, is_connected: List[List[int]]) -> int:
        uf = UnionFind(len(is_connected[0]))

        for y in range(len(is_connected)):
            for x in range(len(is_connected[0])):
                if x == y:
                    continue
                if is_connected[y][x] == 1:
                    uf.union(x, y)

        for x in range(len(is_connected[0])):
            self.ans.add(uf.find(x))

        return len(self.ans)

assert Solution().find_circle_num([[1,1,0],[1,1,0],[0,0,1]]) == 2
assert Solution().find_circle_num([[1,1,1],[1,1,1],[1,1,1]]) == 1
assert Solution().find_circle_num([[1,0,0],[0,1,0],[0,0,1]]) == 3
