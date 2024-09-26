class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        left = right = 0
        p_dict = {}
        for char in p:
            if char not in p_dict:
                p_dict[char] = 1
            else:
                p_dict[char] += 1
        
        output = []
        for i in range(len(p)):
            if s[right] in p_dict:
                p_dict[s[right]] -= 1
            right += 1
            if all(v == 0 for v in p_dict.values()):
                output.append(left)
                
        while right < len(s):
            
            if s[right] in p:
                p_dict[s[right]] -= 1
                
            if s[left] in p:
                p_dict[s[left]] += 1
                        
            left += 1
            right += 1
            if all(v == 0 for v in p_dict.values()):
                output.append(left)
        return output