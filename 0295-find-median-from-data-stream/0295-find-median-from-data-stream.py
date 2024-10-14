class MedianFinder:

    def __init__(self):
        self.arr = []
        self.odd = -1

    def addNum(self, num: int) -> None:
        if len(self.arr) % 2 == 0:
            self.odd += 1
        self.arr.append(num)
        

    def findMedian(self) -> float:
        self.arr.sort()
        return self.arr[self.odd] if len(self.arr) % 2 == 1 else (self.arr[self.odd + 1] + self.arr[self.odd]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()