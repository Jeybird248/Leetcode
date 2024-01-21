class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        arr1, arr2 = [], []
        for num in nums1:
            if num not in nums2:
                arr1.append(num)
        for num in nums2:
            if num not in nums1:
                arr2.append(num)
        return [arr1, arr2]