class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        # Create a 2D DP array with (m+1) x (n+1) dimensions
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Initialize the first row and column of the DP table
        for i in range(m + 1):
            dp[i][0] = i  # Deleting all characters from word1
        for j in range(n + 1):
            dp[0][j] = j  # Inserting all characters into word1 to make word2
        # Fill in the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  # Characters match, no new operation needed
                else:
                    dp[i][j] = min(
                        dp[i - 1][j] + 1,  # Delete character from word1
                        dp[i][j - 1] + 1,  # Insert character into word1
                        dp[i - 1][j - 1] + 1  # Replace character in word1
                    )
        
        # The bottom-right corner of the DP table contains the answer
        return dp[m][n]
