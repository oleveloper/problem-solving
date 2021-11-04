class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ret = 0
        l = nums1 + nums2
        l.sort()
        
        medidx = int(len(l) / 2)
        if (len(l) % 2 == 0):
            ret = (l[medidx - 1] + l[medidx]) / 2
        else:
            ret = l[medidx]
            
        return ret
