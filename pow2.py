class Solution:
    def pow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            x = 1 / x
            n = -n

        result = 1
        while n > 0:
            if n % 2 == 1:
                result *= x
            # THE METHOD: by halving the exponent and squaring the base
            x *= x
            n //= 2

        return result

if __name__ == '__main__':
    test = Solution()
    x = 2.0
    n = 3
    print(test.pow(x, n))
