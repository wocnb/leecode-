class Solution:
    def jump(self, nums: List[int]) -> int:
        maxpos = 0
        current = 0
        times = 0
        n = len(nums)
        for i in range(n-1):
            maxpos = max(maxpos, i + nums[i])
            if i == current:
                
                times += 1
                current = maxpos
        return times

