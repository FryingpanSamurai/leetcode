class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        my_num = int("".join([str(num) for num in digits]))
        my_num += 1
        return [int(ltr) for ltr in str(my_num)]
        


            

if __name__ == '__main__':
    digits = [1,9]
    test = Solution()
    test.plusOne(digits)