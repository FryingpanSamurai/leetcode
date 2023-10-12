import math

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: list[list[int]]) -> int: 
        # a point is valid if it shares the same x-coord or y-coord as [x,y]
        # 'my location': [x,y]
        # brute force sirrr
        # traverse array of points
        # minimize the manhattan distance if more than one
        man_dist = math.inf
        idx = -1
        for i, v in enumerate(points):
            if points[i][0] == x or points[i][1] == y:
                temp_dist = abs(x-points[i][0]) + abs(y-points[i][1])
                if (temp_dist) < man_dist:
                    man_dist = temp_dist
                    idx = i
        return idx if man_dist != math.inf else idx


if __name__ == '__main__':
    x = 3
    y = 4
    points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
    test = Solution()
    test.nearestValidPoint(x,y,points)