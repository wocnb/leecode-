class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.t = {}


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tree = self.t
        for w in word:
            if w in tree:
                pass
            else:
                tree[w] = {}
            tree = tree[w]  
            #词w对应一个字典
        tree['#'] = '#'  
        #字典中有一个#作为标志这是一个单独的词，其值可以是任意的


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tree = self.t
        for a in word:
            if a not in tree:
                return False
            tree = tree[a]
        if "#" in tree: 
            return True
        return False


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tree = self.t
        #print(tree)
        for a in prefix:
            if a not in tree:
                return False
            tree = tree[a]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
