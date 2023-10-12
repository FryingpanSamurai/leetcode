class Solution:
    def arraySign(self, nums: list[int]) -> int:
        def signFunc(p):
            if p > 0:
                return 1
            elif p == 0:
                return 0
            else:
                return -1
        product = 1
        # get the product of nums
        for i in range(len(nums)):
            product *= nums[i]
        return signFunc(product)

if __name__ == '__main__':
    nums = [-1,-2,-3,-4,3,2,1]
    # expected output = 1
    test = Solution()
    test.arraySign(nums)