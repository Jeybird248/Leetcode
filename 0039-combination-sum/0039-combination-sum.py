class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        output = []
        
        def backtrack(curr_arr, index):
            if sum(curr_arr) == target:
                output.append(curr_arr[:])
                return
            if sum(curr_arr) > target:
                return
            for i in range(index, len(candidates)):
                curr_arr.append(candidates[i])
                backtrack(curr_arr, i)
                curr_arr.pop()
        
        backtrack([], 0)
        return output