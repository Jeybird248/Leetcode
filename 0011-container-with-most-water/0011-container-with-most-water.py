class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxArea = min(height[left], height[right]) * (right - left)
        while left < len(height) and left < right:
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
                
            maxArea = max(min(height[left], height[right]) * (right - left), maxArea)
        return maxArea