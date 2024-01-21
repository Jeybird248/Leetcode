class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        arr1, arr2 = set(), set()
        for num in nums1:
            if num not in nums2:
                arr1.add(num)
        for num in nums2:
            if num not in nums1:
                arr2.add(num)
        return [list(arr1), list(arr2)]