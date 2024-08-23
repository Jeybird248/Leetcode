class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtrack(start: int):
            # Base case: if the start index is at the end of the list, add the permutation to the result
            if start == len(nums):
                result.append(nums[:])
                return
            
            # Generate permutations by swapping each element with the start index
            for i in range(start, len(nums)):
                # Swap element at start with element at i
                nums[start], nums[i] = nums[i], nums[start]
                # Recurse with the next index
                backtrack(start + 1)
                # Backtrack by swapping back
                nums[start], nums[i] = nums[i], nums[start]
        
        # Start the backtracking from index 0
        backtrack(0)
        return result