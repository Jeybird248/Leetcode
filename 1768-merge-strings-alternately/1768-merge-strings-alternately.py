class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""
        one = True
        while word1 and word2:
            if one:
                output += word1[0]
                word1 = word1[1:]
            else:
                output += word2[0]
                word2 = word2[1:]
            one = not one
        if word1:
            output += word1
        if word2:
            output += word2
        return output