class Solution:
    def multiplyStrings(self, num1: str, num2: str) -> str:
        temp = list()
        sum = 0
        carry = 0
        zeroes = 1
        big = num1 if len(num1) > len(num2) else num2
        small = num2 if big == num1 else num1

        # loop through both numbers (in rev) to simulate multiplication
        for i in range(len(small)-1, -1, -1):
            carry = 0
            for j in range(len(big)-1, -1, -1):
                # product of the multiplication *remember to add carry
                prod = int(small[i]) * int(big[j]) + carry

                # bring 'ones' digit
                temp.insert(0, str(prod)[0]) if len(str(prod)) == 1 else temp.insert(0, str(prod)[1])

                # if the product is double digits, then we have to carry the integer
                if prod > 9:
                    carry = int(str(prod)[0])
                else:
                    carry = 0

            if carry > 0:
                temp.insert(0, str(carry))

            sum += int(''.join(temp))
            # bring down a zero
            temp = list('0'*zeroes)
            zeroes += 1


        return str(sum)

        

if __name__ == '__main__':
    test = Solution()
    num1 = '123'
    num2 = '456'
    print(test.multiplyStrings(num1, num2))