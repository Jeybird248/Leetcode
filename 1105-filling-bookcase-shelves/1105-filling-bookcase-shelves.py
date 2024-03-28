class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            width, height = books[i - 1]
            dp[i] = dp[i - 1] + height
            j = i - 1
            while j > 0 and width + books[j - 1][0] <= shelfWidth:
                width += books[j - 1][0]
                height = max(height, books[j - 1][1])
                dp[i] = min(dp[i], dp[j - 1] + height)
                j -= 1
                # print(dp)
        return dp[n]