class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        
        dp = [[0] * (n + 1) for _ in range(m + 1)] # length looking at neither string is 0
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]: # looking at indexes i and j
                    dp[i][j] = dp[i - 1][j - 1] + 1 # max characters before are matching + this current character
                else:  
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) # take max characters before matching 
        
        return dp[m][n]