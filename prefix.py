class Solution:
    """
    Prefix sum solutions requires us to pre-process the array before running main logic.
    Output an array with running sum.
    """
    def prefix(nums):
        output = [nums[0]]
        n = len(nums)
        for i in range(1, n):
            output.append(nums[i] + output[len(output) - 1])
        return print(output)
    
if __name__ == "__main__":
    nums = [5, 2, 1, 6, 3, 8]
    Solution()
    Solution.prefix(nums)