class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        maxCount = count = 0
        left, right = 0, k - 1
        
        
        for char in s[0:k]:
            if char in vowels:
                count += 1
        maxCount = count
        # print(left, right, s[left], s[right], count)
        while right < len(s):
            right += 1
            if right < len(s):
                if s[left] in vowels:
                    count -= 1
                if s[right] in vowels:
                    count += 1
                left += 1
                # print(left, right, s[left], s[right], count)
            maxCount = max(maxCount, count)
        return maxCount