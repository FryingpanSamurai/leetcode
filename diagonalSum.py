class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        # loop thru matrix indexes that are equal
        # meaning x = y in coord pos on the mat
        # secondary diagonal
        # len - 1, len - 2, len - 3 ...
        # [0][len-1], [1][len-1-1],


        # i.e. 2x2 mat => sum [0][0], [1][1], [0][1], [1][0]
        sum = 0
        middle = None

        # if mat is odd length we need to exclude the number from the
        # second diagonal's sum
        if len(mat) % 2 == 1:
            middle = len(mat) // 2


        # primary diagonal
        for i in range(len(mat)):
            sum += mat[i][i]

        for j in range(len(mat)):
            if middle is not None and i == middle:
                continue
            else:
                sum += mat[j][len(mat[j]) - 1 - j]

        return sum

if __name__ == '__main__':
    mat = [[7,3,1,9],[3,4,6,9],[6,9,6,6],[9,5,8,5]]
    test = Solution()
    print(test.diagonalSum(mat))