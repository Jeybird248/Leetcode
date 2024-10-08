class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for string in strs:
            s = "".join(sorted(string))
            if s in d:
                d[s].append(string)
            else:
                d[s] = [string]
        return d.values()