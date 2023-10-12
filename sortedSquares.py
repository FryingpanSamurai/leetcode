class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        return sorted([x**2 for x in nums])
    
if __name__ == "__main__":
    nums = [-4, -1, 0, 3, 10]
    test = Solution()
    test.sortedSquares(nums)
