class Solution:
    def reverse(self, x: int) -> int:
        def s(l):
            num1 = 0
            num = len(l)
            for i in range(num-1, -1, -1):
                #print(l[i])
                k = 10 ** i
                num1 += k * int(l[i])
            return num1

        Max = 2**31 -1
        Min = -2**31
        set1 = list()
        str1 = str(x)
        leng = len(str1)
        if str1[0] == '-':
            for i in range(1,leng):
               set1.append(str1[i])
            x = s(set1)
            sss = 0 - x
        else:
            for i in range(leng):
                set1.append(str1[i])
            sss = s(set1)
        if sss > Max:
            return 0
        elif sss < Min:
            return 0
        else:
            return sss
