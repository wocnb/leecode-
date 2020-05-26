class Solution:
    def reverseBits(self, n: int) -> int:
        k = bin(n)
        str1 = k[2:].zfill(32)[::-1]
        str2 = '0b' + str(str1)
        sss = int(str2, 2)
        return sss
