class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        # the difference btw any two consecutive numbers is equal
        # [3, 5, 1]
        # sort the array
        # then loop thru array and check the differences
        # brute force method
        # we could also consider the formula for an arithmetic progression
        # derive the variables, plug and chug baby
        arr.sort()
        increment = arr[0] - arr[1]
        for i in range(1, len(arr)-1):
            if (arr[i] - arr[i+1]) == increment:
                continue
            else:
                return False
        return True
    
    def canMaketwo(self, arr: list[int]) -> bool:
        import math
        arr.sort()
        
        # result of the arithmetic progression function
        # should equal the sum of the array
        a = arr[0]
        l = arr[len(arr) - 1]
        n = len(arr)
        d = arr[1] - arr[0]
        ap_sum = (n/2)*(a + l)

        if math.fsum(arr) == ap_sum:
            return True
        else:
            return False

if __name__ == '__main__':
    test = Solution()