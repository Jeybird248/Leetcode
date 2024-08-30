class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        
        def recursion(curr_arr):
            if curr_arr not in output:
                output.append(curr_arr)
            if not curr_arr:
                return
            for idx in range(len(curr_arr)):
                recursion(curr_arr[:idx] + curr_arr[idx + 1:])
        recursion(nums)
        return output