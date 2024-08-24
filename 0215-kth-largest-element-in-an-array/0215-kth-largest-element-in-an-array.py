class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Initialize an empty min-heap
        minheap = []
        
        # Iterate over all elements in the input array
        for num in nums:
            # Push the current number onto the heap
            heappush(minheap, num)
            # If the heap size exceeds k, remove the smallest element
            if len(minheap) > k:
                heappop(minheap)
        
        # The root of the heap is the k-th largest element
        return minheap[0]