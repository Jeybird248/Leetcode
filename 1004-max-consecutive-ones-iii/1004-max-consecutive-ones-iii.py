class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = right = 0
        max_len = 0
        zero_count = 0

        while right < len(nums):
            if not nums[right]:
                zero_count += 1

            while zero_count > k:
                if not nums[left]:
                    zero_count -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
            right += 1

        return max_len