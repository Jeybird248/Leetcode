class Solution:
    def divisorGame(self, n: int) -> bool:
        alice = True
        while 0 < n:
            if n % 2 == 0:
                n -= 1
            else:
                if n == 1:
                    return not alice
                for i in range(n - 1, 0, -1):
                    if n % i == 0:
                        n -= i
                        break
                
            alice = not alice
        return alice
            