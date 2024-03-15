"""
2. Initialize a dynamic programming array dp of size n + 1, where n is the length of the input string. Set dp[0] and dp[1] to 1, as there is one way to decode an empty string and a string of length 1.
3. Iterate through the string starting from index 2 up to n + 1.

    Convert the current one-digit and two-digit substrings to integers.
    If the one-digit substring is not '0', update dp[i] by adding dp[i - 1] because we can consider the current digit as a single character.
    If the two-digit substring is between 10 and 26 (inclusive), update dp[i] by adding dp[i - 2] because we can consider the current two digits as a single character.

4.The final result is stored in dp[n], where n is the length of the input string.
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, len(s) + 1):
            one_digit = s[i - 1]
            two_digit = s[i - 2:i]
            if int(one_digit):
                dp[i] += dp[i-1]
            if 10 <= int(two_digit) <= 26:
                dp[i] += dp[i - 2]
        return dp[-1]