class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mappings = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        output = []
        
        def recursion(curr_digits, curr_string):
            if len(curr_string) == len(digits):
                output.append(curr_string)
                return
            for letter in mappings[curr_digits[0]]:
                recursion(curr_digits[1:], curr_string + letter)
        recursion(digits, "")
        return output
            