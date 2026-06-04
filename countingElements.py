class Solution:
	def countingElements(arr):
		"""
		Count how many elements x there are, such that x + 1 is also in arr.
		Count duplicates separately.
		"""
		my_set = set(arr)
		my_count = 0
		for i in arr:
			if i+1 in my_set:
				my_count += 1

		return my_count


if __name__ == "__main__":
	arr = [1,2,3]
	arr2 = [1,1,3,3,5,5,7,7]
	Solution()
	print(Solution.countingElements(arr2))
