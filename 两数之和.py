class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol = list()
        for i in range(len(nums)):
            ac = target - nums[i]
            if ac in nums:
                num2 = nums.index(ac)
                if num2 == i:
                    pass
                else:
                    return i, num2
                    
                    break
        #return sol
