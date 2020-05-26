class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if 0 not in nums:
            return True
        elif len(nums) < 2:
            return True
        elif nums[0] >= len(nums):
            return True
        n = len(nums)
        now = nums[0]
        for i in range(1, n-1):
            if i <= now:
                now = max(now, i + nums[i])
        ans = (now >= n-1)
        return ans

