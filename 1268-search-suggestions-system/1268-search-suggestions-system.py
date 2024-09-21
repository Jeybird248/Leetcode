class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = {}
        for word in sorted(products):
            curr = root
            for letter in word:
                if letter not in curr:
                    curr[letter] = {"#suggestions": []}
                curr = curr[letter]
                if len(curr["#suggestions"]) < 3:
                    curr["#suggestions"].append(word)
                    
                    
        curr = root
        results = []

        for char in searchWord:
            # Move to the next node
            if char in curr:
                curr = curr[char]
                results.append(curr.get("#suggestions", []))
            else:
                # If no such prefix exists, append empty suggestions for the remaining characters
                results.append([])
                curr = {}  # no further traversal, just empty lists from now on

        return results