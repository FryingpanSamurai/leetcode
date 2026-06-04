from collections import defaultdict

class Solution:
	def checkEqualOccurrences(s):
		"""
		Given a string, s:
		determine if all characters have the same frequency
		"""
		counts = defaultdict(int)

		# lets make a hash map of the frequency
		# and then compare the values in the map
		for c in s:
			counts[c] += 1

		# my_count = counts[s[0]]
		# for k in counts:
		# 	if counts[k] != my_count:
		# 		return False
		# return True

		# BETTER METHOD: get the values of the map, not the keys
		# then put the values into a set, if the resulting set is 
		# length of one, then its true (freq is the same for all)
		frequencies = counts.values()
		return len(set(frequencies)) == 1

		# BONUS: collections Counter one-liner
		# return len(set(Counter(s).values())) == 1


if __name__ == "__main__":
	s = "abacbc"
	s2 = "aaabb"
	Solution()
	print(Solution.checkEqualOccurrences(s2))