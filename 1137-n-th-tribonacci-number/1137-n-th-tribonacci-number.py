class Solution:
    def __init__(self):
        self.arr = [0, 1, 1]
    def tribonacci(self, n: int) -> int:
        if n <= 2:
            return self.arr[n]
        for i in range(n - 2):
            self.arr.append(sum(self.arr))
            self.arr.pop(0)
        return self.arr[-1]