class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = defaultdict(int)
        for num in arr:
            d[num] += 1
        return sorted(list(set(d.values()))) == sorted(list(d.values()))