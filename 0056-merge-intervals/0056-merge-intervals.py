class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        output = []
        left, right = intervals[0][0], intervals[0][1]
        
        for idx, interval in enumerate(intervals[1:]):
            if right >= interval[0]:
                right = max(right, interval[1])
                left = min(left, interval[0])
            else:
                output.append([left, right])
                left = interval[0]
                right = interval[1]
                
        output.append([left, right])
        return output
        