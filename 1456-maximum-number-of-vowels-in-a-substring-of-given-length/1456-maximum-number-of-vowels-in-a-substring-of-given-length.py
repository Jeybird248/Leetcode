class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        left = right = 0
        currSum = maxSum = 0
        for i in range(k):
            if s[right] in vowels:
                currSum += 1
            right += 1
        maxSum = currSum
        while right < len(s):
            if s[left] in vowels:
                currSum -= 1
            if s[right] in vowels:
                currSum += 1
            maxSum = max(currSum, maxSum)
            left += 1
            right += 1
        return maxSum