class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output = []
        for candy in candies:
            output.append(candy + extraCandies >= max(candies))
        return output