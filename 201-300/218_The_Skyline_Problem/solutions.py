from typing import List


class Solution:
    @classmethod
    def get_sky_line(cls, buildings: List[List[int]]) -> List[List[int]]:
        group_list = []

        cur_min_x1 = buildings[0][0]
        cur_min_x2 = buildings[0][1]

        building_group = []
        for building in buildings:
            if building[1] <= cur_min_x2:
                building_group.append(building)
            elif building[1] > cur_min_x2:
                cur_min_x1 = building[0]
                cur_min_x2 = building[1]

                group_list.append((cur_min_x1, cur_min_x2, building_group))
                building_group = []

        print(group_list)

# FORMAT : X1, X2, HEIGHT
# Input : [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
# Output : [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]


print(Solution.get_sky_line([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]))
