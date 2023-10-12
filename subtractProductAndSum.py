class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        # return difference btw the product of its digits and the sum of its digits
        temp = str(n)
        sum = 0
        product = 1
        for x in temp:
            sum += int(x)
            product *= int(x)
        return product - sum



if __name__ == '__main__':
    n = 234
    test = Solution()
    test.subtractProductAndSum(n)