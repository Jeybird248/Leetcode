class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output = []
        
        def backtrack(start, path):
            # base case: if start index reaches the end of the string, add the path to output
            if start == len(s):
                output.append(path)
                return
            
            # explore all possible end positions for substring
            for end in range(start + 1, len(s) + 1):
                # if the substring is a palindrome, recursively continue partitioning
                if (s[start:end] == s[start:end][::-1]):
                    backtrack(end, path + [s[start:end]])
        
        backtrack(0, [])
        return output