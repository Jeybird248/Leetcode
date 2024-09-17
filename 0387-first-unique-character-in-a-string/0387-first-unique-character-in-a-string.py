class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = Counter(s)
        if 1 not in d.values():
            return -1
        for key in d.keys():
            if d[key] == 1:
                return s.index(key)
        return -1