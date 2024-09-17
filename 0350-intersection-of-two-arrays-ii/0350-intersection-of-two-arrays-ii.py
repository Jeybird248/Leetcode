class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = Counter(nums1)
        d2 = Counter(nums2)
        output = []
        for key in d1.keys():
            if key in d2.keys():
                for i in range(min(d1[key], d2[key])):
                    output.append(key)
        return output