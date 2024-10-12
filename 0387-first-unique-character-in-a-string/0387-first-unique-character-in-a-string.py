class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = Counter(s)
        if 1 not in d.values():
            return -1
        else:
            for i in d.keys():
                if d[i] == 1:
                    return s.index(i)
        return -1