class Solution:
    def maxArea(self, height: List[int]) -> int:
        low = 0
        high = len(height) - 1
        ans = 0
        while high > low:
            if height[low] < height[high]:
                area = height[low] * (high - low)
                ans = max(area, ans)
                low += 1
            elif height[low] >= height[high]:
                area = height[high] * (high - low)
                ans = max(area, ans)
                high -= 1
        return ans
