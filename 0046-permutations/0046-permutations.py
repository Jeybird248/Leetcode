class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        visited = [False for _ in range(len(nums))]
        
        def backtrack(curr_arr):
            if len(curr_arr) == len(nums):
                output.append(curr_arr[:])
            else:
                for i in range(len(nums)):
                    if not visited[i]:
                        curr_arr.append(nums[i])
                        visited[i] = True
                        backtrack(curr_arr)
                        visited[i] = False
                        curr_arr.pop()
        backtrack([])
        return output