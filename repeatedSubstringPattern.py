class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # calculate the length of the string
        n = len(s)
        n = len(s)
        # try only those substring lengths that are factors of the length of the string
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                # check only those substrings that start at the beginning of the string
                if s[:i] * (n // i) == s:
                    return True
        
        return False
        

                


if __name__ == '__main__':
    s = 'abaababaab'
    test = Solution()
    test.repeatedSubstringPattern(s)