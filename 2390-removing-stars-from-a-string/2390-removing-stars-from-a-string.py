class Solution:
    def removeStars(self, s: str) -> str:
        left = 0
        for _ in range(len(s)):
            if s[left] == "*":
                s = s[:left - 1] + s[left + 1:]
                left -= 2
            left += 1
        return s