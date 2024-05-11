class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        word = str1 if len(str1) < len(str2) else str2
        maxLen = 0
        for index in range(1, len(word) + 1):
            if word[:index] * (len(str1) // index) == str1 and word[:index] * (len(str2) // index) == str2:
                maxLen = index
        return word[:maxLen]