class Solution:
    def translateNum(self, num: int) -> int:
        s = str(num)
        dp = [0] * (len(s)+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, len(s)+1):
            num1 = int(s[i-2])
            num2 = int(s[i-1])
            num3 = num1 * 10 + num2
            if 10 <= num3 <= 25:
                dp[i] = dp[i-1] + dp[i-2] 
            elif 0 <= num3 < 10 or 25 < num3:
                dp[i] = dp[i-1] 
        return dp[-1]
