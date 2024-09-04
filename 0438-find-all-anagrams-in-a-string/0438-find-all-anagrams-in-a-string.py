class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left = right = 0
        output = []
        d = defaultdict(int)
        for char in p:
            d[char] += 1
            
        while right < len(s):
            if right >= len(p):
                d[s[left]] += 1
                left += 1
            d[s[right]] -= 1
            right += 1
            if all(v == 0 for v in d.values()):
                output.append(left)

        return output