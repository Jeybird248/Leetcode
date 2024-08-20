class Solution:
    def climbStairs(self, n: int) -> int:
        # 0 = 0, 1 = 1, 2 = 2, 3 = 3
        # 1 + 1 + 1+ 1,    1+ 2 +1,   2+ 2,    2+ 1+ 1,    1+ 1+ 2
        arr = [0] * (n + 1)
        arr[0] = 1
        arr[1] = 1
        for i in range(2, n + 1):
            arr[i] = arr[i - 1] + arr[i - 2]

        return arr[-1]
            