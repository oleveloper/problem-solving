class Solution:
   
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            while left < right:
                s = nums[left] + nums[right] + nums[i]
                if s < 0:
                    left += 1
                elif s > 0:
                    right -= 1
                else:
                    result.append([nums[left], nums[right], nums[i]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                    
        return result
