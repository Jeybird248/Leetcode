class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])  # Sort pairs based on the second element
        longest = 1  # Initialize longest to 1
        prev_end = pairs[0][1]  # Initialize prev_end to the end of the first pair
        for pair in pairs[1:]:  # Iterate through pairs starting from the second pair
            if pair[0] > prev_end:  # If the start of the current pair is greater than the end of the previous pair
                longest += 1  # Increment the length of the chain
                prev_end = pair[1]  # Update prev_end to the end of the current pair
        return longest  # Return the length of the longest chain
