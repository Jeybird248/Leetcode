class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pointer1 = m - 1
        pointer2 = n - 1
        pointer3 = m + n - 1
        while pointer1 >= 0 and pointer2 >= 0:
            if nums1[pointer1] >= nums2[pointer2]:            
                nums1[pointer3] = nums1[pointer1] 
                pointer1 -= 1
            else:
                nums1[pointer3] = nums2[pointer2]
                pointer2 -= 1
            pointer3 -=1
    
        while pointer2 >= 0 and pointer3 >= 0:
            nums1[pointer3] = nums2[pointer2]
            pointer2 -= 1
            pointer3 -=1