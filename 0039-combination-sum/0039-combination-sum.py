class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.output = []
        def backtrack(currIdx, path, curr_target):
            print(path, curr_target)
            if curr_target == 0:
                self.output.append(list(path))
                return
            if curr_target < 0:
                return
            
            for i in range(currIdx, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, curr_target - candidates[i])
                path.pop()
            
        backtrack(0, [], target)
        
        return self.output