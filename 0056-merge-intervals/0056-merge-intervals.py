class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        length = len(intervals)
        intervals.sort(key=lambda x: x[0])
        left, right = intervals[0][0], intervals[0][1]
        
        for idx, interval in enumerate(intervals[1:]):
            if right >= interval[0]:
                right = max(right, interval[1])
                left = min(left, interval[0])
            else:
                intervals.append([left, right])
                left = interval[0]
                right = interval[1]
                
        intervals.append([left, right])
        return intervals[length:]
        