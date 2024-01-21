class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        d1, d2 = defaultdict(int), defaultdict(int)
        for letter in word1:
            d1[letter] += 1
        for letter in word2:
            d2[letter] += 1
        return sorted(d1.values()) == sorted(d2.values()) and sorted(d1.keys()) == sorted(d2.keys())