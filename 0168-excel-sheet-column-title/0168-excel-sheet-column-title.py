class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        output = ""
        while columnNumber > 0:
            columnNumber -= 1  # adjust for 1-based index
            char = chr(columnNumber % 26 + ord('A'))  # calculate the character
            output = char + output  # prepend the character to the output
            columnNumber //= 26  # move to the next digit
        return output