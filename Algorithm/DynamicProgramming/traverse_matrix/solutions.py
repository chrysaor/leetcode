class Solution:
    def __init__(self):
        self.ans = 0
        self.matrix = []

    def init_mat(self, rows, cols):
        """Initiation solution matrix
        :type rows: int
        :type cols: int
        """
        self.matrix = [[0] * cols for _ in range(rows)]

    def find_path_dp(self, rows: int, cols: int) -> None:
        """Find a path with a table - O(M * N)"""
        # SETTING TRIVIAL UNIQUE PATH
        for row in range(rows):
            self.matrix[row][0] = 1

        for col in range(cols):
            self.matrix[0][col] = 1

        # FILL A MATRIX WITH DP TABLE -> CURRENT WAY = UP WAY + LEFT WAY
        for row in range(1, rows):
            for col in range(1, cols):
                self.matrix[row][col] = self.matrix[row][col-1] + self.matrix[row-1][col]

    def find_path_graph(self, rows: int, cols: int, x: int, y: int) -> None:
        """Find a path with recursive O(|V| + |E|)
        :type rows: int
        :type cols: int
        :type x: int
        :type y: int
        """
        if x >= rows or y >= cols:
            return

        # FIND PATH COUNT
        self.matrix[x][y] += 1

        # MOVE RIGHT
        if -1 < x < cols and -1 < y < rows:
            self.find_path_graph(rows, cols, x, y+1)

        # MOVE DOWN
        if -1 < x < cols and -1 < y < rows:
            self.find_path_graph(rows, cols, x+1, y)

    def unique_paths(self, rows: int, cols: int) -> int:
        """Find unique path
        :type rows: int
        :type cols: int
        :rtype: int
        """
        self.init_mat(rows, cols)
        self.find_path_dp(rows, cols)

        for row in range(rows):
            print(self.matrix[row])

        return self.matrix[rows-1][cols-1]


if __name__ == '__main__':
    print(Solution().unique_paths(5, 5))
