import math

class Solution:
    def countOdds(self, low: int, high: int) -> str:
        # given two non-neg int low and high
        # return count of odd numbers btw low and high (inclusive)

        # we could just do it by math
        # there are high - low/2 odd numbers between x - y
        if low % 2 == 0 and high % 2 == 0:
            return int((high - low)/2)
        elif low % 2 == 1 and high % 2 == 1:
            return int(((high - low)/2) + 1)
        else:
            out = math.ceil((high-low)/2)
            return out

    
if __name__ == "__main__":
    high = 22
    low = 21
    test = Solution()
    test.countOdds(low, high)

