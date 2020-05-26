class Solution:
    def longestPalindrome(self, s: str) -> str:
        if(not s or len(s)==1):
            return s
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        max_len= 1
        start = 0
        for i in range(n):
            dp[i][i] = True
            if(i < n-1 and s[i] == s[i+1]):
                dp[i][i+1] = True
                start = i
                max_len = 2

        for length in range(3, n+1):
            for starts in range(n+1-length):
                end = starts + length -1
                if (s[starts] == s[end] and dp[starts+1][end-1]):
                    dp[starts][end] = True
                    start = starts
                    max_len = length
        return s[start:start+max_len]
