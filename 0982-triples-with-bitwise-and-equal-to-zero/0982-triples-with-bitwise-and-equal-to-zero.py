class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        res = 0
        freq = defaultdict(int)
        n = len(nums)
        for i in range(n):
            for j in range(n):
                t = nums[i]&nums[j]
                freq[t] += 1
        for n in nums:
            for t in freq:
                if n&t == 0:
                    res += freq[t]
        return res
