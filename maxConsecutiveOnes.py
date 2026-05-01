class Solution:
    def maxConsecutiveOnes(nums, k):
        """
        GOAL:   Given a binary array, nums and an integer k- return the max number of consecutive ones
                in which you can flip at most k 0's
        """
        ans = count = start = end = 0
        n = len(nums)

        # iter through array
        for end in range(n):
            # check if new value is 0
            if nums[end] == 0:
                count += 1

            # manage our zero count if we are over allotted value
            while count > k:
                if nums[start] == 0:
                    count -= 1
                start += 1
            ans = max(ans, end - start + 1)

        return print(ans)
    
if __name__ == "__main__":
    nums = [1,1,1,0,0,0,1,1,1,1,0]
    k = 2
    Solution()
    Solution.maxConsecutiveOnes(nums, k)