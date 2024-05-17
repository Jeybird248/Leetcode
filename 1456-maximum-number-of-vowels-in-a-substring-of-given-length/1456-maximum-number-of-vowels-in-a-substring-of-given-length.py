class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeoiu"
        start = 0
        end = k - 1
        maxCount = 0
        for i in range(k):
            maxCount = maxCount + 1 if s[i] in vowels else maxCount
        currCount = maxCount
        while end < len(s) - 1:
            end += 1
            currCount = currCount + 1 if s[end] in vowels else currCount
            currCount = currCount - 1 if s[start] in vowels else currCount
            start += 1
            maxCount = max(maxCount, currCount)
        return maxCount