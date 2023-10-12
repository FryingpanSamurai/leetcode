class Solution:
    def thirdMaxNumber(self, nums: list[int]) -> int:
        # the goal would ideally be
        # sort the list into descending order
        # with only distinct values (track duplicates through dict or use a set)
        # then just output position 3 or len(sorted)
        myset = set(nums)
        nums = [x for x in myset]
        nums.sort()

        for i, num in enumerate(nums):
            if len(nums) >= 3 and i == len(nums) - 3:
                return num
            elif i == len(nums) - 1:
                return num
            
if __name__ == "__main__":
    nums = [-1, 2, 3]
    test_ob = Solution()
    test_ob.thirdMaxNumber(nums)
