class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        m = len(A)
        n = len(B)
        dp = list()
        for i in range(m+1):
            dp.append([0]*(n+1))
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                #print(i)
                if A[i] == B[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]


