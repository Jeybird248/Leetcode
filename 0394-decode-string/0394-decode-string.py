class Solution:
    def decodeString(self, s: str) -> str:
        numbers = []
        strings = []
        current_string = ""
        current_number = 0
        
        for char in s:
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            elif char == "[":
                numbers.append(current_number)
                strings.append(current_string)
                current_string = ""
                current_number = 0
            elif char == "]":
                current_string = strings.pop() + current_string * numbers.pop()
            else:
                current_string += char
        return current_string
                