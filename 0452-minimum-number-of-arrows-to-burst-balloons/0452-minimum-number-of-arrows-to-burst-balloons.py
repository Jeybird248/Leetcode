class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        shots = len(points)
        points = sorted(points, key=lambda point: point[1])
        currS, currE = points[0][0], points[0][1]
        print(points)
        for point in points[1:]:
            # print(currS, currE, point, shots)
            if currE >= point[0]:
                shots -= 1
                currS = currE - point[0]
            else:
                currS = point[0]
                currE = point[1]
            
        return shots