class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        curr = self.root
        for char in (word + "\0"):
            if char in curr:
                curr = curr[char]
            else:
                curr[char] = {}
                curr = curr[char]
        

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char in curr:
                curr = curr[char]
            else:
                return False
        return "\0" in curr

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char in curr:
                curr = curr[char]
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)