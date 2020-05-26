class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        sol = list()
        def ch(c, d):
            x = 2*c
            num1 = -d/x
            return num1
        if a != 0:
            k = ch(a, b)
            low = 0
            high = len(nums) - 1
            while low <= high:
                if abs(nums[high] - k) > abs(nums[low] - k):
                    x = nums[high]
                    high -= 1
                else:
                    x = nums[low]
                    low += 1

                y = a*x*x + b*x + c
                sol.append(y)
            if a > 0:
                return sol[::-1]
            elif a < 0:
                return sol
        elif a == 0:
            for i in nums:
                y = i*b + c
                sol.append(y)
            if b > 0:
                return sol
            else:
                return sol[::-1]
