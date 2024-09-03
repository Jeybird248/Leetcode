class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        n = int(bin(n)[2:])
        while n:
            count += (n & 1)
            n  = n // 10
            
        return count