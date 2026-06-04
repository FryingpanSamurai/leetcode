class Solution:
	def missingNumber(nums):
		"""
		Given an array nums containing n distinct numbers in the range [0, n]
		return the only number in the range that is missing from the array
		"""
		nums_set = set([i for i in range(len(nums) + 1)])
		
		for n in nums_set:
			if n in nums:
				continue
			else:
				return n


if __name__ == "__main__":
	nums = [3,0,1]
	Solution()
	print(Solution.missingNumber(nums))
	