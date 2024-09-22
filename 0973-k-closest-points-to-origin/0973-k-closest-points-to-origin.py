class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        # Iterate over each point
        for x, y in points:
            # Calculate the squared Euclidean distance (no need to compute the square root, since it's unnecessary for comparison)
            distance = x**2 + y**2

            # Push a tuple with (-distance, [x, y]) into the heap
            heapq.heappush(max_heap, (-distance, [x, y]))

            # If the heap exceeds size k, remove the farthest point
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        # Extract the coordinates from the heap
        return [coord for _, coord in max_heap]
