class Solution:
    """
    GOAL:   Given an array(int) length n
            Find contiguous subarrary, whose length is equal to k,
            that has a maximum average value
    """
    def maxAverageSubarray(nums, k):
        current = 0

        # build first window
        for i in range(k):
            # add nums in the fixed length of k and divide by k
            current += nums[i]
        ans = current / k

        # now we'll iter through the complete array with our fixed window, updating our average as needed
        for i in range(k, len(nums)):
            # expand the window
            current += nums[i] - nums[i - k]
            ans = max(ans, current / k)

        return print(ans)

if __name__ == "__main__":
    nums = [1,12,-5,-6,50,3]
    k = 4
    Solution()
    Solution.maxAverageSubarray(nums, k)
