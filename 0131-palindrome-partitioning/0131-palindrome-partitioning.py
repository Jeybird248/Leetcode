class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output = []
        def backtrack(currIdx, path):
            if currIdx == len(s):
                output.append(path)
                return
            for i in range(currIdx + 1, len(s) + 1):
                if s[currIdx:i] == s[currIdx:i][::-1]:
                    backtrack(i, path + [s[currIdx:i][::-1]])
                
        backtrack(0, [])
        return output