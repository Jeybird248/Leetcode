class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()  # Sort the array to make duplicate handling easier
        visited = [False] * len(nums)  # Keep track of used elements
        
        def backtrack(curr_arr):
            if len(curr_arr) == len(nums):  # Base case: if permutation is complete
                output.append(curr_arr[:])  # Make a copy of curr_arr and add it to output
                return
            
            for i in range(len(nums)):
                # Skip duplicates: if the current number is the same as the previous one,
                # and the previous one hasn't been used in the current permutation path.
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue
                
                if not visited[i]:
                    visited[i] = True  # Mark the element as used
                    curr_arr.append(nums[i])  # Add the current number to the permutation
                    backtrack(curr_arr)  # Recurse to continue building the permutation
                    curr_arr.pop()  # Backtrack by removing the last element
                    visited[i] = False  # Unmark the element as used
        
        backtrack([])  # Start the recursion with an empty permutation
        return output
