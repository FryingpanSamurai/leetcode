class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        # monotone increasing if for all i <= j, nums[i] <= nums[j]
        # ""       decreasing if for all i <= j, nums[i] >= nums[j]
        increasing = False
        decreasing = False

        for i in range(len(nums)-1):
            increment = nums[i] - nums[i+1]
            if increment > 0 and not increasing:
                decreasing = True
                continue
            elif decreasing and increment < 0:
                return False
            elif increasing and increment > 0:
                return False
            elif increment == 0:
                continue
            else:
                increasing = True
        return True

    def isMono(self, nums: list[int]) -> bool:
        increasing = decreasing = True

        for i in range(len(nums)-1):
            if nums[i] > nums[i + 1]:
                increasing = False
            elif nums[i] < nums[i + 1]:
                decreasing = False
        
        return increasing or decreasing


if __name__ == '__main__':
    nums = [1,1,-1, 1]
    test = Solution()
    test.isMonotonic(nums=nums)
    test.isMono(nums=nums)