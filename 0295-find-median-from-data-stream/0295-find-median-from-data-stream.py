class MedianFinder:

    def __init__(self):
        self.arr = []
        
    def addNum(self, num: int) -> None:
        left, right = 0, len(self.arr) - 1
        
        # Binary search for the correct insertion point
        while left <= right:
            mid = (left + right) // 2
            if self.arr[mid] < num:
                left = mid + 1
            else:
                right = mid - 1
        
        # Insert the number at the correct position
        self.arr.insert(left, num)
        
    def findMedian(self) -> float:
        n = len(self.arr)
        if n % 2 == 1:
            return self.arr[n // 2]
        else:
            return (self.arr[n // 2 - 1] + self.arr[n // 2]) / 2


# Example of usage:
# obj = MedianFinder()
# obj.addNum(1)
# obj.addNum(2)
# print(obj.findMedian()) # Outputs 1.5
# obj.addNum(3)
# print(obj.findMedian()) # Outputs 
