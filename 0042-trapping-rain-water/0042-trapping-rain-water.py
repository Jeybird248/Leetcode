class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxLeft, maxRight = 0, 0
        output = 0
        while left < right:
            if height[left] <= height[right]:
                if maxLeft - height[left] > 0:
                    output += maxLeft - height[left]
                maxLeft = max(maxLeft, height[left])
                left += 1
            else:
                if maxRight - height[right] > 0:
                    output += maxRight - height[right]
                maxRight = max(maxRight, height[right])
                right -= 1
        
        return output