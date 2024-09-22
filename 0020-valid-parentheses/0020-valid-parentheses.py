class Solution:
    def isValid(self, s: str) -> bool:
        q = []
        paran = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }
        
        for char in s:
            if char in paran:
                q.append(paran[char])
            else:
                if not q or char != q.pop():
                    return False
        return not q