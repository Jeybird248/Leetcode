class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        d = {
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"],
        }
        
        output = []
        
        def recursion(curr_str, curr_d):
            if len(curr_str) == len(digits):
                output.append(curr_str[:])
                return
            for num in d[curr_d[0]]:
                recursion(curr_str + num, curr_d[1:])
        
        recursion("", digits)
        return output