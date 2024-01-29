class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        output = []
        for spell in spells:
            left, right = 0, len(potions) - 1
            count = 0

            while left <= right:
                mid = left + (right - left) // 2
                if potions[mid] * spell >= success:
                    count += (right - mid) + 1
                    right = mid - 1
                else:
                    left = mid + 1

            output.append(count)

        return output