class Solution:
    def knightDialer(self, n: int) -> int:
        connections = {
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            5: [],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6]
        }
        
        mod = 10**9 + 7
        
        dp = {i: 1 for i in range(10)}
        for _ in range(n - 1):
            next_dp = {}
            for i in range(10):
                next_dp[i] = sum(dp[j] for j in connections[i]) % mod
            dp = next_dp
        
        return sum(dp.values()) % mod
