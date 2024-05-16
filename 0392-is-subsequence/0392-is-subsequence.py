class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if not s:
            return True
        start = end = 0
        for i in range(len(t)):
            # print("comparing start to i", s[start], t[i])
            # print()
            if s[start] == t[i]:
                end = start
                for j in range(i, len(t)):
                    # print("comparing end to j", s[end], t[j])
                    if end < len(s) and t[j] == s[end]:
                        end += 1
                    if end == len(s):
                        return True
        return False