class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        idx = 0

        tmp = [x for x in nums if x > target]
        idx = len(nums) - len(tmp)
        if target in nums: idx = nums.index(target)
            
        return idx
