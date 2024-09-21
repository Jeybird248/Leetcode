class Solution:
    def partition(self, s: str) -> List[List[str]]:
        output = []
        
        def backtrack(curr_arr, index):
            if index == len(s):
                output.append(curr_arr[:])
            else:
                for i in range(index + 1, len(s) + 1):
                    if s[index: i] == s[index: i][::-1]:
                        curr_arr.append(s[index: i])
                        backtrack(curr_arr, i)
                        curr_arr.pop()
                        
        backtrack([], 0)
        return output