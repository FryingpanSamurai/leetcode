class Solution:
    def minStartVal(self, nums):
        """
        GOAL:   Simplification: we need to find a min pos value (ans) such that the running sum (s) never goes below 1.

                1. min value is 1
                2. iter over array and find the lowest value, this tells us the min val that the runnning sum will have.
                    - if s >= 0, return min poss value of ans, 1
                    - if s < 0, return a value such that it never goes below 1 (-s + 1)
                        because adding -s gives us min val 
        """
        sum = 0
        ans = 0

        # start running sum, retrieving the lowest number
        # then its the absolute value of that number plus one
        # thus we quickly get the startValue without playing "the guess game"
        for n in nums:
            sum += n
            ans = min(ans, sum)
        return -ans + 1
            
    
if __name__ == "__main__":
    nums = [-3,2,-3,4,2]
    Solution()
    Solution.minStartVal(nums)