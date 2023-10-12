class Solution:
    def lengthOfLastWord(self, s: str) -> int: 
        # return the len of the last word in the string
        return len(s.split()[-1])

if __name__ == '__main__':
    s = "hello world"
    test = Solution()
    test.lengthOfLastWord(s)