class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiou"
        arr = []
        for letter in s:
            if letter.lower() in vowels:
                arr.append(letter)
        output = ""
        for letter in s:
            if letter.lower() in vowels:
                output += arr.pop()
            else:
                output += letter
        return output
        