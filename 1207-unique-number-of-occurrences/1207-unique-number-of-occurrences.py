class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        s = defaultdict(int)
        valueCounts = []
        for num in arr:
            s[num] += 1
        for num in s:
            if s[num] in valueCounts:
                return False
            else:
                valueCounts.append(s[num])
        return True

