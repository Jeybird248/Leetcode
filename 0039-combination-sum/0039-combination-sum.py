class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        
        def backtrack(currTarget, curr_arr, currIdx):
            if currTarget == 0:
                output.append(curr_arr[:])
                return
            if currTarget < 0:
                return
            for idx, c in enumerate(candidates[currIdx:]):
                curr_arr.append(c)
                backtrack(currTarget - c, curr_arr, currIdx + idx)
                curr_arr.pop()
                
        backtrack(target, [], 0)
        return output