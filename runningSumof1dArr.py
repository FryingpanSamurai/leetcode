class Solution:
    def runningSum(nums):
        # this is just implementing a prefix array
        output = [nums[0]]
        n = len(nums)
        for i in range(1, n):
            output.append(nums[i] + output[len(output) - 1])
        return output
    
if __name__ == "__main__":
    nums = [1,2,3,4]
    Solution()
    Solution.runningSum(nums)