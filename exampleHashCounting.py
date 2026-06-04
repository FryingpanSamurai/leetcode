from collections import defaultdict

class Solution:
	def example(self,s,k):
		"""
		Find the length of the longest substring that contains at most k distinct characters.

		e.g. s = "eceba" and k = 2, return 3; "ece"
		"""
		# k distinct elements, sounds like a sliding window
		# however, this is still an O(n) time complexity, 
		# using hash map we can check the constraint in O(1)

		counts = defaultdict(int)
		left = ans = 0

		for right in range(len(s)):
			counts[s[right]] += 1

			# len of counts is the number of distinct keys
			# if we go over the amount of distinct keys (k),
			# we need to shrink the window until we are back 
			# within limitations
			while len(counts) > k:
				# 'shrinking the window' entails 
				# 1. decrementing the hash map value
				# 2. removing keys that don't have a count
				# 3. shrink the window
				counts[s[left]] -= 1
				
				if counts[s[left]] == 0:
					del counts[s[left]]
				left += 1

			ans = max(ans, right - left + 1)
		return ans


if __name__ == "__main__":
	s = 'eceba'
	mySolution = Solution()
	print(mySolution.example(s=s,k=2))
	