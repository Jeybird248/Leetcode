class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        def backtrack(curr_arr, idx):
            if curr_arr not in output:
                output.append(curr_arr.copy())
            for i in range(idx + 1, len(nums)):
                curr_arr.append(nums[i])
                backtrack(curr_arr, i)
                curr_arr.pop()
        backtrack([], -1)
        return output