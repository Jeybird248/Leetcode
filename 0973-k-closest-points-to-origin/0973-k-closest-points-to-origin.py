from heapq import heappush, heappushpop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for point in points:
            dist = -(point[0] ** 2 + point[1] ** 2)  # use negative distance to simulate max-heap
            if len(heap) < k:
                heappush(heap, (dist, point))  # push distance as the first element
            else:
                heappushpop(heap, (dist, point))  # replace farthest point if necessary
        
        return [x[1] for x in heap]  # extract points from heap
