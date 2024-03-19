class Solution:
    def numDecodings(self, s: str) -> int:
        # Modulo value
        MOD = 10**9 + 7
        
        # Base cases
        if not s or s[0] == "0":
            return 0
        
        # Initialize dp array
        dp = [0] * (len(s) + 1)
        dp[0], dp[1] = 1, 9 if s[0] == "*" else 1

        # Dynamic Programming
        for i in range(2, len(s) + 1):
            one_digit = s[i - 1]
            two_digit = s[i - 2:i]

            if one_digit == "*":
                dp[i] += 9 * dp[i - 1]
            elif one_digit != "0":
                dp[i] += dp[i - 1]

            if two_digit == "**":
                dp[i] += 15 * dp[i - 2]  # 15 combinations from 11 to 26
            elif two_digit[0] == "*":
                if two_digit[1] == "*":
                    dp[i] += 9 * dp[i - 2]  # For '**', 9 possibilities for first '*' and 9 for second '*'
                elif '0' <= two_digit[1] <= '6':
                    dp[i] += 2 * dp[i - 2]  # For '*1' to '*6', 2 possibilities for first '*' and 1 for second '*'
                else:
                    dp[i] += dp[i - 2]  # For '*7' to '*9', 1 possibility for first '*' and 1 for second '*'
            elif two_digit[1] == "*":
                if two_digit[0] == "1":
                    dp[i] += 9 * dp[i - 2]  # For '1*', 9 possibilities for second '*'
                elif two_digit[0] == "2":
                    dp[i] += 6 * dp[i - 2]  # For '2*', 6 possibilities for second '*'
            elif 10 <= int(two_digit) <= 26:
                dp[i] += dp[i - 2]

            # Apply modulo to avoid overflow
            dp[i] %= MOD

        return dp[-1]
