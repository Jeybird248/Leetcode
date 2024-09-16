class Solution:
    def intToRoman(self, num: int) -> str:
        d = {
            1000 : "M",
            900 : "CM",
            500 : "D",
            400 : "CD",
            100 : "C",
            90 : "XC",
            50 : "L",
            40 : "XL",
            10 : "X",
            9 : "IX",
            5 : "V",
            4 : "IV",
            1 : "I",
        }
        
        output = ""
        
        while num:
            for integer in d.keys():
                if integer <= num:
                    output += d[integer]
                    num -= integer
                    break
        return output