from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        
        def backtrack(remaining, curr_combination, index):
            # base case: if the remaining target is 0, we found a valid combination
            if remaining == 0:
                output.append(curr_combination)
                return
            
            # if remaining target is less than 0, no valid combination is possible
            if remaining < 0:
                return
            
            # explore further elements from the current index onwards
            for i in range(index, len(candidates)):
                # recurse with updated parameters: new target, updated combination, and current index
                backtrack(remaining - candidates[i], curr_combination + [candidates[i]], i)
        
        # initial call to backtrack with full target, empty combination, and starting index 0
        backtrack(target, [], 0)
        
        return output
