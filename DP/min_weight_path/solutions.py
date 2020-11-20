class Solution:
    def minimumPathCost(self, triangle):
        """Calculate minimum path triangle
        [
          [5],
          [1,6],
          [4,3,10],
          [3,2,4,1]
        ]
        :type triangle: list of list of int
        :rtype: int
        """

        # Exceptional case
        if triangle is None or len(triangle) == 0:
            return 0

        # Trivial case
        if len(triangle) == 1:
            return triangle[0][0]

        current_path = 0
        sum_path = triangle[0][current_path]

        for idx in range(1, len(triangle)):
            current_line = triangle[idx]
            first, second = (current_path, 0), (current_path + 1, 0)
            # print(first, second)

            if 0 <= current_path:
                first = (current_path, current_line[current_path])

            if current_path < len(current_line) - 1:
                second = (current_path + 1, current_line[current_path + 1])

            min_val, min_sum = min([first, second], key=lambda x: x[1])

            current_path = min_val
            sum_path += min_sum

        return sum_path


table = [
    [5],
    [2, 3],
    [4, 3, 10],
]

print(Solution().minimumPathCost(table))
