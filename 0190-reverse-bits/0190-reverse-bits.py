class Solution:
    def reverseBits(self, n: int) -> int:
        flipped = str(bin(n))[::-1][:-2]
        return int(flipped + "0" * (32 - len(flipped)), 2)