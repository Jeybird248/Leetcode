class Solution:
    def removeStars(self, s: str) -> str:
        # stack - LIFO, removes latest
        # queue - FIFO, removes first
        output = []
        for char in s:
            if char == "*":
                if output:
                    output.pop()
            else:
                output.append(char)
        return "".join(output)