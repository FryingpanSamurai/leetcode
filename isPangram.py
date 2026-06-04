class Solution:
	def checkPangram(self, s):
		myalphabet = "abcdefghijklmnopqrstuvwxyz"
		my_set = set(s)
		for l in myalphabet:
			if l in my_set:
				continue
			else:
				return False
		return True


if __name__ == "__main__":
	s = "thequickbrownfoxjumpsoverthelazydog"
	mySolution = Solution()
	print(mySolution.checkPangram(s))