class Solution:
    def rob(self, nums: List[int]) -> int:
        p2 = p1 = 0
        for i in nums:
            p2, p1 = p1, max(p1, p2 + i)
        return p1