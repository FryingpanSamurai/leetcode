class Solution:
    """
    FUNCTION: Return largest perimeter of a triangle with non-zero area
    PARAMS: nums as list of integers representing side lengths(?)
    OUTPUT: the largest perimeter of a triangle formed from any combination of these lengths
            output zero if impossible to form a triangle
    """
    def largestPerimeter(self, nums: list[int]) -> int:
        # QUESTIONS
        # how do I know what lengths can form a triangle
        # condition a + b > c
        # apparently this is over my fucking head
        # sort the list
        # [1,1,2,10]
        # reverse traverse
        # condition 1 + 2 > 10
        # condition 1 + 1 > 2
        # THE ASSUMPTION IS THAT A, B, C ARE IN CORRESPONDING ORDER OF THE TRIPLET WE ARE EXAMINING
        # ... im actually so dumb frfr
        nums.sort()
        for i in range(len(nums) - 3, -1, -1):
            if nums[i] + nums[i+1] > nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0

if __name__ == '__main__':
    nums = [1,2,1,10]
    test = Solution()
    test.largestPerimeter(nums)