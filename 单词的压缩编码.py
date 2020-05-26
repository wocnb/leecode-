class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        word = set(words)
        sum = 0
        for i in words:
            for j in range(1, len(i)):
                try:
                    word.remove(i[j:])
                except:
                    pass
        for k in word:
            sum += len(k) + 1
        return sum
