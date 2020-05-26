class Solution:
    def decodeString(self, s: str) -> str:
        stack = list()
        times = 0
        res = ''
        for ch in s:
            if ch == '[':
                stack.append([res, times])
                res = ''
                times = 0
            elif ch == ']':
                res1, times1 = stack.pop()
                res = res1 + res * times1
            elif '0' <= ch <= '9':
                times = times *10 + int(ch)
            else:
                res += ch
        return res
