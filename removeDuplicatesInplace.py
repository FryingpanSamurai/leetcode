class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # remove duplicate in-place
        # do not allocate any extra 
        for i in range(len(nums) - 2):
            if nums[i] == nums[i+1]:
                
        return len(nums)