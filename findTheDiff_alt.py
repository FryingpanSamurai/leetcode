class Solution:
    def findTheDifference(self, s: str, t: str) -> str: 
        # SAME AS FINDTHEDIFFERENCE.py BUT USING A XOR ALGORITM
        # XOR TABLE
        # 0 ^ 0 = 0
        # 0 ^ 1 = 1
        # 1 ^ 0 = 1
        # 1 ^ 1 = 0

        # ALGORITHM
        # 1. init a var ch which would hold the xor'd results
        # 2. xor all the characters with ch while iterating thru str s
        # 3. xor all the chars with ch while iterating thru string t
        # (could combine steps 2 & 3) 
        # 4. return ch as answer

        # 1.
        ch = 0

        # 2.
        for ltr in s:
            ch ^= ord(ltr)

        for ltr in t:
            ch ^= ord(ltr)
        
        # what is left after XOR'ing everything is the difference
        return chr(ch)

if __name__ == '__main__':
    test = Solution()