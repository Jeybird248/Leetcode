from typing import List

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
                print(s[start:end], path, start, end)
                if is_palindrome(s[start:end]):
                    backtrack(end, path + [s[start:end]])

        def is_palindrome(substring: str) -> bool:
            return substring == substring[::-1]

        # start backtracking from the beginning of the string
        backtrack(0, [])
        return output
