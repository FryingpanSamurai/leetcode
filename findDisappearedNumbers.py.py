class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        # Given an array nums of n integers 
        # where nums[i] is in the range [1, n], 
        # 
        # return an array of all the integers in the range [1, n] 
        # that do not appear in nums.

        # instantiate excluded nums list
        excluded = []

        # we're gonna do full brute force method
        mydict = {}
        # append number range to dict
        for i in range(1, len(nums) + 1):
            mydict[i] = 0
        
        # mark the numbers that have occured in the range
        for v in nums:
            mydict[v] = 1
        
        # go thru our dict and find the missing numbers
        for v in mydict:
            if mydict.get(v) == 0:
                excluded.append(v)

        return excluded
        
        
            

if __name__ == "__main__":
    nums = [2, 1, 3, 5]
    test_ob = Solution()
    test_ob.findDisappearedNumbers(nums)