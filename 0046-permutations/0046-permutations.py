class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        def recursion(curr_arr, remaining_arr):
            if len(nums) == len(curr_arr):
                output.append(curr_arr[:])
            remaining_arr = remaining_arr.copy()
            for i in range(len(remaining_arr)):
                num = remaining_arr[i]
                new_curr = curr_arr + [num]
                new_remaining = remaining_arr[:i] + remaining_arr[i+1:]
                recursion(new_curr, new_remaining)           
            
        recursion([], nums)
        return output
                