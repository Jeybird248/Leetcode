class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == t:
            return True
        s_point = t_point = 0
        while t_point < len(t) and s_point < len(s):
            if t[t_point] == s[s_point]:
                s_point += 1
            t_point += 1
        return s_point >= len(s)