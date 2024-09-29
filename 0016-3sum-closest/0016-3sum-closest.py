class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        print(nums)
        closestSum = float("inf")
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                val = nums[left] + nums[right] + nums[i]
                # print(nums[i], nums[left], nums[right], "total:", val)
                closestSum = val if abs(val - target) < abs(closestSum - target) else closestSum
                if val == target:
                    return target
                elif val - target > 0:
                    right -= 1
                else:
                    left += 1
        return closestSum
                