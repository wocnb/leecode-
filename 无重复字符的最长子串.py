class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        maxlength = 0
        current = 0
        ac = list()
        pointer = 0
        for i in range(n):
            current += 1
            while(s[i] in ac):
                ac.remove(s[pointer])
                pointer += 1
                current -= 1
            if current >= maxlength:
                maxlength = current
            ac.append(s[i])
        return maxlength
