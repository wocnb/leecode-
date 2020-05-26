class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        count = list()
        n = 0
        def c(n):
            n1 = 0
            item = bin(n).count('1')
            #print(item)
            '''for i in range(len(item)):
                #print(item[i])
                if item[i] == '1':
                    n1 += 1'''
            #print(n1)
            return item
            #print(n)
            
        list1 = sorted(arr, key = lambda x: (c(x),x))
        return list1
