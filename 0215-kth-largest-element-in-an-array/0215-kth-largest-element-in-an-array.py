class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = nums[:k]
        heapq.heapify(min_heap)

        # Iterate through the remaining elements in the array
        for num in nums[k:]:
            if num > min_heap[0]:
                # If the current number is larger than the smallest in the heap, replace the root
                heapq.heappushpop(min_heap, num)

        # The root of the min-heap is the kth largest element
        return min_heap[0]