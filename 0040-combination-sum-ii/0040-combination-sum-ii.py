class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        output = []
        print(candidates)
        def backtrack(curr_arr, index, target):
            if target == 0:
                output.append(curr_arr[:])
                return
            for i in range(index, len(candidates)):
                # skip duplicate numbers
                if i > index and candidates[i] == candidates[i - 1]:
                    continue

                # break early if the current number exceeds the target
                if candidates[i] > target:
                    break

                curr_arr.append(candidates[i])
                backtrack(curr_arr, i + 1, target - candidates[i])
                curr_arr.pop()  # backtrack to try next candidate
        
        backtrack([], 0, target)
        return output