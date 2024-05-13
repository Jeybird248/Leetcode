class Solution:
    def compress(self, chars: List[str]) -> int:
        output = []
        length = 0
        currChar = ""
        for char in chars:
            if char != currChar:
                if currChar:
                    output.append(currChar)
                if length > 1:
                    for num in str(length):
                        output.append(num)
                length = 1
                currChar = char
            else:
                length += 1
        if currChar:
            output.append(currChar)
        if length > 1:
            for num in str(length):
                output.append(num)
        chars[:] = output
        return len(output)