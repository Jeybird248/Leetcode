class Solution:
    def findMinDifference(self, timePoints: list[str]) -> int:
        # Convert each time to minutes
        def timeToMinutes(t: str) -> int:
            hours, minutes = map(int, t.split(":"))
            return hours * 60 + minutes
        
        # Convert all time points to minutes and sort them
        minutes_list = sorted([timeToMinutes(t) for t in timePoints])
        # print(minutes_list)
        # Initialize the minimum difference to be large
        min_diff = float('inf')
        
        # Calculate the difference between consecutive times
        for i in range(1, len(minutes_list)):
            min_diff = min(min_diff, minutes_list[i] - minutes_list[i - 1])
        
        # Handle the circular difference (last time point to first time point)
        circular_diff = 1440 + minutes_list[0] - minutes_list[-1]
        min_diff = min(min_diff, circular_diff)
        
        return min_diff
