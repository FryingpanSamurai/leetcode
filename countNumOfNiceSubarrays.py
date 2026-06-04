from collections import defaultdict

class Solution:
	def oddNumbers(nums, k):
		counts = defaultdict(int)
		counts[0] = 1
		ans = curr = 0

		for n in nums:
			curr += n % 2
			ans += counts[curr - k]
			counts[curr] += 1
		return ans


if __name__ == "__main__":
	nums = [1,1,2,1,1]
	k = 3
	Solution()
	print(Solution.oddNumbers(nums, k))
	