class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Check if the total sum of the array is odd
        summed = sum(nums)
        if summed % 2:
            return False

        # Initialize a set to store possible sums
        dp = set()
        dp.add(0)
        
        # Calculate the target sum
        target = summed // 2
        
        # Iterate through the array in reverse order
        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            # Iterate through the sums in the current set
            for t in dp:
                # If the sum plus the current number equals the target, return True
                if (t + nums[i]) == target:
                    return True
                # Add the sum plus the current number and the current sum to the next set
                nextDP.add(t + nums[i])
                nextDP.add(t)
                # print(nextDP, target, t, nums[i])
            # Update the current set
            dp = nextDP
            
        
        # If no partition found, return False
        return False