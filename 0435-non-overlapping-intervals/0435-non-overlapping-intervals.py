class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) <= 1:
            return 0
        intervals = sorted(intervals, key=lambda x:x[1])
        count = 0
        currS, currE = intervals[0][0], intervals[0][1]
        for interval in intervals[1:]:
            if currE > interval[0]:
                count += 1
            else:
                currS = interval[0]
                currE = interval[1]
            # print(currS, currE, interval)
        return count