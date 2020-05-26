class Solution:
    def cuttingRope(self, n: int) -> int:
        s = [1]*(n+1)
        for i in range(2, n+1):
            for j in range(1, i):
                s[i] = max(s[i], s[j]*(i-j), s[i-j]*j, s[i-j]*s[j], j*(i-j))
        return s[n]
