class Solution:
    def isHappy(self, n: int) -> bool:
        sums = []
        while n != 1:
            s = 0
            while n:
                s += (n % 10) ** 2
                n //= 10
            if s in sums:
                return False
            sums.append(s)
            n = s
            
        return True