class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s 
        n = len(s)
        res = list()
        count = 0
        flag = 1
        ans = ''
        for i in range(numRows):
            s1 = ''
            res.append(s1)
        for i in range(n):
            res[count] += s[i]
            count += flag
            if count == numRows-1 or count == 0:
                flag = -flag
        for i in range(numRows):
            ans += res[i]
        return ans
