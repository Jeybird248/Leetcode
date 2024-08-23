class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        def traversal(curr_arr, size, remaining):
            if len(curr_arr) == size:
                output.append(curr_arr)
            for i in range(len(remaining)):
                copy = remaining.copy()
                a  = copy.pop(i)
                # curr_arr.append(a)
                traversal(curr_arr + [a], size, copy)
        traversal([], len(nums), nums)
        return output