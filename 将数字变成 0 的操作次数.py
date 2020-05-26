class Solution:
    def numberOfSteps (self, num: int) -> int:
        def c(n):
            if n % 2 == 0:
                k = n / 2
            elif n % 2 == 1:
                k = n - 1
            #print(k)
            return k
        time = 1
        num1 = c(num)
        if num1 == -1:
            time = 0
        else:
            while(num1 > 0):
                num1 = c(num1)
                time += 1
        return time
