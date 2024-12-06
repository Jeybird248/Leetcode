class Trie:

    def __init__(self):
        self.map = {}

    def insert(self, word: str) -> None:
        curr = self.map
        # print(curr)
        for c in word + ".":
            if c in curr:
                curr = curr[c]
            else:
                curr[c] = {}
                curr = curr[c]
        
    def search(self, word: str) -> bool:
        curr = self.map
        # print(curr)
        for c in word + ".":
            if c in curr:
                curr = curr[c]
            else:
                return False
        return True

    def startsWith(self, prefix: str) -> bool:
        curr = self.map
        # print(curr)
        for c in prefix:
            if c in curr:
                curr = curr[c]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)