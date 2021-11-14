class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        tmp = list(set(nums))
        tmp.sort()
        for i, v in enumerate(tmp):
            nums[i] = v

        return len(tmp)
