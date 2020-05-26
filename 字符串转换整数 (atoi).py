import re
class Solution:
    def myAtoi(self, str: str) -> int:
        MAX = 2**31-1
        MIN = -2**31
        check = re.match('[ ]*([\+\-]?\d+)', str)
        print(check)
        if check:
            num = int(check.group(1))
            if num > MAX:
                return MAX
            elif num < MIN:
                return MIN
            else:
                return num
        else:
            return 0

            #matches = re.match('[ ]*([+-]?\d+)', str)
