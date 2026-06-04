from collections import defaultdict

class Solution:
	def intersectionMultArr(nums):
		"""
		Given a 2D arr nums, that contain n arrays of distinct nums:
		return a sorted array containing all nums that appear in all n arrays
		"""
		# lets use a hash map to keep track of frequency,
		# then we can iter through the keys of the map
		# and if the count is equal to n (number of arrays)
		# then it will be included in our sorted output array
		counts = defaultdict(int)
		for arr in nums:
			for n in arr:
				counts[n] += 1

		n = len(nums)
		ans = []
		for k in counts:
			if counts[k] == n:
				ans.append(k)

		return sorted(ans)


if __name__ == "__main__":
	nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
	Solution()
	print(Solution.intersectionMultArr(nums))
	