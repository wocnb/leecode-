class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        B = list()
        for i in range(len(A)):
            b = A[i]**2
            B.append(b)
        
        B.sort()
        #print(A)
        return B
