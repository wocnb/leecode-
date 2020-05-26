class Solution:
    def isHappy(self, n: int) -> bool:
        def check(num):
            s = str(num)
            sum = 0
            for i in s:
                #print(i)
                sum += int(i) * int(i)
            return sum #shu
        result = list()
        res = check(n)
        result.append(res)
        while(res):
            res = check(res)
            #print(result)
            if res == 1:
                return True
            elif res in result:
                return False
            result.append(res)
