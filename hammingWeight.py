class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
                

if __name__ == '__main__':
    n = bin(-3)
    test = Solution()
    test.hammingWeight(n)