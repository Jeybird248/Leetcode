class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        output = 0
        for num in nums:
            d[num] += 1
        for num in nums:
            if num == k / 2:
                output += d[num] // 2
                d[num] = 0
            else:
                output += min(d[num], d[k - num])
                d[num] = 0
                d[k - num] = 0
        return output