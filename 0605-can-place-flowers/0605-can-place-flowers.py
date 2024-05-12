class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            if (flowerbed[0] == 0 and n <= 1) or n <= 0:
                return True
            else:
                return False
        for i in range(len(flowerbed)):
            if i == 0 and flowerbed[i] == 0 and flowerbed[1] == 0:
                n -= 1
                flowerbed[i] = 1
            elif i == len(flowerbed) - 1 and flowerbed[i] == 0 and flowerbed[i - 1] == 0:
                n -= 1
                flowerbed[i] = 1
            elif flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                n -= 1
                flowerbed[i] = 1
        return n <= 0