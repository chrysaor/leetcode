class Solution:
    def __init__(self):
        self.ans = 0
        self.matrix = []

    def init_mat(self, rows, cols):
        for row in range(rows):
            self.matrix.append([0 for _ in range(cols)])

    def find_path(self, rows: int, cols: int, x: int, y: int) -> None:
        """Find a path with recursive O(2^n)"""
        if x >= rows or y >= cols:
            return

        # FIND PATH COUNT
        self.matrix[x][y] += 1

        # MOVE RIGHT
        if -1 < x < cols and -1 < y < rows:
            self.find_path(rows, cols, x, y+1)

        # MOVE DOWN
        if -1 < x < cols and -1 < y < rows:
            self.find_path(rows, cols, x+1, y)

    def unique_paths(self, rows: int, cols: int) -> int:
        """Find unique path
        :type rows: int
        :type cols: int
        :rtype: int
        """
        self.init_mat(rows, cols)
        self.find_path(rows, cols, 0, 0)

        for row in range(rows):
            print(self.matrix[row])

        return self.matrix[rows-1][cols-1]


print(Solution().unique_paths(3, 3))
