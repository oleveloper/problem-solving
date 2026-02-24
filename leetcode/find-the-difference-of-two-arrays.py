class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        li1, li2 = set(nums1), set(nums2)
        return [list(li1 - li2), list(li2 - li1)]
