"""

    Check if n is equal to 0. If it is, then there is only 1 possible number with unique digits, which is 0. Return 1 as the result.
    If n is greater than 10, then the count will be the same as countNumbersWithUniqueDigits(10) because for n > 10, there will be repetition, and the count will not change anymore. Therefore, set n to min(n, 10).
    Start with a base count of 10, since we can always have 0 to 9 as the first digit. We will add more numbers to this count as we go along.
    For the second digit, we can have 9 choices, since 0 is already used. For the third digit, we can have 9 choices again, since we cannot repeat the first or second digit. For the fourth digit, we can have 8 choices, and so on. The total count is the product of the number of choices for each digit.
    Therefore, for i from 2 to n, compute the number of choices for each digit and add it to the count.
    Return the count as the result.

"""

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if not n:
            return 1
        n = min(n, 10)
        
        count  = 10
        for i in range(2, n + 1):
            choices = 9
            for j in range(i - 1):
                choices *= 9 - j
            count += choices
        return count