class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Think about how you can recursively build subsets by deciding for each element 
        in the array whether to include it in the current subset or not. Start from an 
        empty set and progressively add or exclude each element. This approach is called 
        "backtracking." How can you ensure you explore all possibilities without repeating subsets?
        """
        
        result = []  # Initialize the result list to store all subsets

        def backtrack(index, current_subset):
            # Base case: if we have considered all elements
            if index == len(nums):
                result.append(current_subset[:])  # Add a copy of the current subset to the result
                return

            # Recursive case: exclude the current element
            backtrack(index + 1, current_subset)

            # Recursive case: include the current element
            current_subset.append(nums[index])
            backtrack(index + 1, current_subset)

            # Backtrack: remove the last element added for the next call
            current_subset.pop()

        # Start the backtracking from index 0 and with an empty subset
        backtrack(0, [])
        return result
