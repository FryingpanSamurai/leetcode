class Solution:
    def numOfWays(nums):
        """
        GOAL:   Find number of ways to split the array into two parts.
                Such that, the first section sum >= second section.
                Where len(second_section) >= 1
        """
        # if we build the prefix array beforehand, we can calculate left and right sums very easy
        # after looking, we don't need each value, so we'll nix the prefix
        total = sum(nums)
        ans = left_section = 0

        # len(nums) - 1 because right section requires at least one value
        for i in range(len(nums) - 1):
            left_section += nums[i]
            # right = total - the left section
            # but if we are just using the total, we don't ever care about the prefix array
            right_section = total - left_section
            if left_section >= right_section:
                ans += 1

        return print(ans)
    
if __name__ == "__main__":
    nums = [40,7,-8,14]
    Solution()
    Solution.numOfWays(nums)