from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        candidates.sort()
        
        def backtrack(curr_arr, index, target):
            if target == 0:
                output.append(curr_arr[:])
                return
            
            for num in range(index, len(candidates)):
                # skip duplicates
                if num > index and candidates[num] == candidates[num - 1]:
                    continue
                # prune branches where target is already smaller
                if candidates[num] > target:
                    break
                curr_arr.append(candidates[num])
                backtrack(curr_arr, num + 1, target - candidates[num])
                curr_arr.pop()
        
        backtrack([], 0, target)
        return output
