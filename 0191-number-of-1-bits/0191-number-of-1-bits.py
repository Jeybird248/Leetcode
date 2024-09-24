class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        binary = bin(n)[2:]
        for char in binary:
            if char == "1":
                count += 1
        return count