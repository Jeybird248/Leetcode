class Solution:
    def numTilings(self, n: int) -> int:
        if n <= 2:
            return n
        a, b, c = 1, 1, 2
        for _ in range(3, n + 1):
            a, b, c = b, c, (c * 2 + a) % (10**9 + 7)
        return c