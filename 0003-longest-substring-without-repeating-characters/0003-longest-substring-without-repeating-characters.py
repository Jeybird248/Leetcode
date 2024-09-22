class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = defaultdict(int)
        left = 0
        maxLen = 0
        for idx, char in enumerate(s):
            d[char] += 1
            while d[char] > 1:
                d[s[left]] -= 1
                left += 1
            else:
                maxLen = max(maxLen, idx - left + 1)
        
        return maxLen