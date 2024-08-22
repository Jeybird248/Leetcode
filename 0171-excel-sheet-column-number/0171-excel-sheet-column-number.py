class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        output = 0
        for char in columnTitle:
            # Compute the value of the current character
            value = ord(char) - ord('A') + 1
            # Update the output considering the base-26 system
            output = output * 26 + value
        return output