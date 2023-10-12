
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        mydict = {}
        done = False
        i = 0
        while not done:
            if i == len(nums) - 1:
                done = True

            # establish variables
            val = nums[i]
            # establish & increment count of current val
            mydict[val] = mydict.get(val, 0) + 1

            # if the current count is more than one (duplicate)
            # we need to remove this value from our list
            if mydict[val] > 1:
                # when we pop a value, current index become next val- no need to increment the index
                nums.pop(i)
            # current count is one or zero
            # advance the pointer
            else:
                i += 1


        return nums




if __name__ == "__main__":
    nums = [1, 1, 2, 3, 5, 8, 8, 8]
    sol = Solution()
    print(sol.removeDuplicates(nums))