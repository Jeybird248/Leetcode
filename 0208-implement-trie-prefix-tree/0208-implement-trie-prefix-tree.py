class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            # If the character is not in the current node, add it
            if char not in node:
                node[char] = {}
            # Move to the next node (child)
            node = node[char]
        # Mark the end of a word with a special character
        node['#'] = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node:
                return False
            # Move to the next node (child)
            node = node[char]
        return '#' in node.keys()

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            # Move to the next node (child)
            node = node[char]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)