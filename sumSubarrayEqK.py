from collections import Counter, defaultdict

class Solution:
	def sumEqualsK(nums, k):
		# remember prefix arrays
		# any difference in the prefix array equal to k
		# represents a subarray with a sum equal to k

		# proof showed prefix up to j - 1 = current - k
		counts = defaultdict(int) 
		counts[0] = 1
		ans = curr = 0

		for num in nums:
			curr += num
			ans += counts[curr - k]
			counts[curr] += 1

		return ans

if __name__ == "__main__":
	nums = [1,2,1,2,1]
	k = 3
	Solution()
	print(Solution.sumEqualsK(nums, k))