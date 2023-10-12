class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # kadanes solution
        cur_sa = nums[0]
        max_sa = nums[0]

        for i in nums[1:]:
            cur_sa = max(i, cur_sa + i)
            max_sa = max(cur_sa, max_sa)

if __name__ == "__main__":
    nums1 = [-4,2,-3,1,2,-5]
    test = Solution()
    test.maxSubArray(nums1)