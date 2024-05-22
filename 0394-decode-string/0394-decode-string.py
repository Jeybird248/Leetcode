class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_string = ""
        current_number = 0
        
        for char in s:
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            elif char == '[':
                # Push the current number and string onto the stack
                stack.append((current_string, current_number))
                # Reset current string and number
                current_string = ""
                current_number = 0
            elif char == ']':
                # Pop from the stack and repeat the current_string
                last_string, number = stack.pop()
                current_string = last_string + number * current_string
            else:
                current_string += char
                
        return current_string
