class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        visited = [False for _ in range(len(nums))]
        def backtrack(curr_arr):
            if len(curr_arr) == len(nums) and curr_arr not in output:
                output.append(curr_arr[:])
                return
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    curr_arr.append(nums[i])
                    backtrack(curr_arr)
                    curr_arr.pop()
                    visited[i] = False
            
        backtrack([])
        return output