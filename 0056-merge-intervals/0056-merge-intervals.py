class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        output = []
        curr_interval = None
        for i in range(len(intervals)):
            if curr_interval and curr_interval[1] >= intervals[i][0]:
                curr_interval[1] = max(curr_interval[1], intervals[i][1])
                curr_interval[0] = min(curr_interval[0], intervals[i][0])
            else:
                if curr_interval:
                    output.append(curr_interval)
                curr_interval = intervals[i]
        if curr_interval:
            output.append(curr_interval)
        return output
            